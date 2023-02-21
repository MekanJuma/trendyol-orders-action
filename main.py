
import requests
import json
from datetime import datetime
import gspread
import pytz
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Orders").sheet1 

headers = {
    'authority': 'auth.trendyol.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'application-id': '1',
    'content-type': 'application/json;charset=UTF-8',
    'culture': 'tr-TR',
    'origin': 'https://auth.trendyol.com',
    'referer': 'https://auth.trendyol.com/static/fragment?application-id=1&storefront-id=1&culture=tr-TR&language=tr&debug=false',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'storefront-id': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

json_data = {
    'email': 'challenger9151@gmail.com',
    'password': 'Atty1991',
}

headers_orders = {
    'authority': 'public-sdc.trendyol.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'cache-control': 'no-cache,no-store',
    'origin': 'https://www.trendyol.com',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

params = {
    'page': '1',
    'sorting': '0',
    'storefrontId': '1',
    'searchText': '',
}





def save_data(orders):
    sheet.append_rows(orders)   # Insert the list as a row at index 4
    print('Done!')

def get_targets():
    data = sheet.get_all_records()
    last_date = data[-1]['Order Date']
    last_order = data[-1]['Order Number']
    
    return [last_date, last_order]

def main():
  print('Update started')
  target_datetime = pytz.timezone('Europe/Istanbul').localize(datetime.strptime(get_targets()[0], "%b %d, %Y %H:%M:%S"))
  target_order = str(get_targets()[1])
  
  with requests.session() as session:
      response = session.post('https://auth.trendyol.com/login', headers=headers, json=json_data)
      access_token = response.json()['accessToken']
      
      headers_orders['authorization'] = f'Bearer {access_token}'
      
      response = session.get('https://public-sdc.trendyol.com/discovery-web-omsgw-service/orders', params=params, headers=headers_orders)
      
      result = response.json()
      result = result['result']
      hasNext = result['hasNext']
      order_length = len(result['orders'])
      orders = [
          [
          order['summary']['fullName'], 
          order['summary']['orderNumber'], 
          datetime.fromtimestamp(order['summary']['orderDate']/1000, pytz.timezone('Europe/Istanbul')).strftime("%b %d, %Y %H:%M:%S"),
          order['summary']['payment']['totalCharges'],
          len(order['items'])
          ]
          for order in result['orders'] if datetime.fromtimestamp(order['summary']['orderDate']/1000, pytz.timezone('Europe/Istanbul')) > target_datetime and str(order['summary']['orderNumber']) != target_order]
  
      print('Orders', orders)
      pageNo = 2
      while hasNext and len(orders) == order_length:
          params['page'] = str(pageNo)
          response = session.get('https://public-sdc.trendyol.com/discovery-web-omsgw-service/orders', params=params, headers=headers_orders)
          if response.status_code == 200:
              data = response.json()
              result_data = data['result']
              hasNext = result_data['hasNext']
              length = len(result_data['orders'])
              orders_in = [
                  [
                  order['summary']['fullName'], 
                  order['summary']['orderNumber'], 
                  datetime.fromtimestamp(order['summary']['orderDate']/1000, pytz.timezone('Europe/Istanbul')).strftime("%b %d, %Y %H:%M:%S"),
                  order['summary']['payment']['totalCharges'],
                  len(order['items'])
                  ]
                  for order in result_data['orders'] if datetime.fromtimestamp(order['summary']['orderDate']/1000, pytz.timezone('Europe/Istanbul')) > target_datetime and str(order['summary']['orderNumber']) != target_order]
              if(length == len(orders_in)):
                  orders.extend(orders_in)
                  print('Page No: ', pageNo)
                  pageNo += 1
              else:
                  print('No more orders')
                  break
          else:
              print('Status code: ' + response.status_code, 'Message: ', response.content)
              break
      
      if len(orders) > 0:
          
          orders = sorted(orders, key=lambda x: x[1])
          
          save_data(orders)
      else:
        print('No orders saved!')



if __name__ == "__main__":
    main()
