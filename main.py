import requests
import json
from datetime import datetime
from config import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def track(data):
    with open('tracker.json', 'w') as outfile:
        json.dump(data, outfile)
    
    print('Saved tracker successfully!!')

def save_data(orders):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Orders").sheet1 
    sheet.append_rows(orders)   # Insert the list as a row at index 4
    print('Done!')

def get_target_date():
    with open('tracker.json', 'r') as f:
        data = json.load(f)
    
    latest_date = data['LastDate']
    return datetime.strptime(latest_date, "%b %d, %Y %H:%M:%S")

def get_target_order():
    with open('tracker.json', 'r') as f:
        data = json.load(f)
    
    return data['LastOrderNumber']


target_datetime = get_target_date()
target_order = get_target_order()

with requests.session() as session:
    response = session.post('https://auth.trendyol.com/login', headers=headers, json=json_data)
    access_token = response.json()['accessToken']
    refresh_token = response.json()['refreshToken']
    
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
        datetime.fromtimestamp(order['summary']['orderDate']/1000).strftime("%b %d, %Y %H:%M:%S"),
        order['summary']['payment']['totalCharges'],
        len(order['items'])
        ]
        for order in result['orders'] if datetime.fromtimestamp(order['summary']['orderDate']/1000) > target_datetime and str(order['summary']['orderNumber']) != target_order]
    
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
                datetime.fromtimestamp(order['summary']['orderDate']/1000).strftime("%b %d, %Y %H:%M:%S"),
                order['summary']['payment']['totalCharges'],
                len(order['items'])
                ]
                for order in result_data['orders'] if datetime.fromtimestamp(order['summary']['orderDate']/1000) > target_datetime and str(order['summary']['orderNumber']) != target_order]
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
        latest_date = max([datetime.strptime(i[2], "%b %d, %Y %H:%M:%S")  for i in orders])
        search = [index for index, order in enumerate(orders) if order[2] == latest_date.strftime("%b %d, %Y %H:%M:%S")]
        latest_index = search[0] if len(search) != 0 else 0
        latest_order = orders[latest_index][1]
        orders = sorted(orders, key=lambda x: x[1])
        
        track({'LastDate': latest_date.strftime("%b %d, %Y %H:%M:%S"), 'LastOrderNumber': latest_order})
        save_data(orders)
    print('No orders saved!')