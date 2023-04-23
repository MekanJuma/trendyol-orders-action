import requests
from datetime import datetime
import time
import gspread
import pytz
from oauth2client.service_account import ServiceAccountCredentials


class TrendyolOrders:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                      "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Orders")

    def authenticate(self):
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

        json_data = {
            'email': self.email,
            'password': self.password,
        }

        with requests.session() as session:
            response = session.post('https://auth.trendyol.com/login', headers=headers, json=json_data)
            access_token = response.json()['accessToken']

        headers_orders['authorization'] = f'Bearer {access_token}'
        return session, headers_orders
    
    def fetch_orders(self, session, headers, sheet_name='Orders', status=None):
        tg_dt, tg_ord = self.get_targets(sheet_name)
        target_datetime = pytz.timezone('Europe/Istanbul').localize(datetime.strptime(tg_dt, "%b %d, %Y %H:%M:%S"))
        target_order = str(tg_ord)
        
        if status:
            url = 'https://public-sdc.trendyol.com/discovery-web-omsgw-service/orders/status'
        else:
            url = 'https://public-sdc.trendyol.com/discovery-web-omsgw-service/orders'

        params = {
            'page': '1',
            'storefrontId': '1',
        }

        if status:
            params['status'] = status
        else:
            params['sorting'] = '0'
            params['searchText'] = ''
        
        orders = []

        while True:
            response = session.get(url, params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                result_data = data['result']
                hasNext = result_data['hasNext']
                length = len(result_data['orders'])
                orders_in = [
                    [
                        order['summary']['fullName'],
                        order['summary']['orderNumber'],
                        datetime.fromtimestamp(order['summary']['orderDate'] / 1000, pytz.timezone('Europe/Istanbul')).strftime("%b %d, %Y %H:%M:%S"),
                        order['summary']['payment']['totalCharges'],
                        len(order['items'])
                    ]
                    for order in result_data['orders']
                    if datetime.fromtimestamp(order['summary']['orderDate'] / 1000, pytz.timezone('Europe/Istanbul')) > target_datetime and str(order['summary']['orderNumber']) != target_order
                ]

                if len(orders_in) > 0:
                    orders.extend(orders_in)
                    if(length != len(orders_in)):
                        break
                else:
                    break

                if not hasNext:
                    break

                print('Page: ', params['page'])
                print('Load Length: ', len(orders))
                params['page'] = str(int(params['page']) + 1)
                time.sleep(1)
            else:
                print('Status code:', response.status_code, 'Message:', response.content)
                break

        return orders
    
    def process_orders(self, session, headers, sheet_name, status=None):
        orders_list = self.fetch_orders(session, headers, sheet_name, status)
        if orders_list and len(orders_list) > 0:
            orders_list = sorted(orders_list, key=lambda x: datetime.strptime(x[2], "%b %d, %Y %H:%M:%S"))
            self.save_data(orders_list, sheet_name)
        else:
            print(f'No {sheet_name.lower()} saved!')
    
    def get_targets(self, sheet_name):
        current_sheet = self.sheet.worksheet(sheet_name)
        data = current_sheet.get_all_records()
        last_date = data[-1]['Order Date']
        last_order = data[-1]['Order Number']
        
        return [last_date, last_order]
    
    def save_data(self, orders, sheet_name):
        current_sheet = self.sheet.worksheet(sheet_name)
        current_sheet.append_rows(orders)
        print('Done!')

if __name__ == '__main__':
    app = TrendyolOrders('challenger9151@gmail.com', 'Atty1991')
    session, headers = app.authenticate()
    app.process_orders(session, headers, sheet_name='Orders')
    app.process_orders(session, headers, sheet_name='Returns', status='Claim')
    app.process_orders(session, headers, sheet_name='Cancelled', status='Cancelled')
