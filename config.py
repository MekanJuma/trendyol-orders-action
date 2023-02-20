headers = {
    'authority': 'auth.trendyol.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'application-id': '1',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'hvtb=1; initialTrafficSource=utmcsr=(direct)|utmcmd=(none)|utmccn=(not set); pid=61KRIzwASe; _tt_enable_cookie=1; _ttp=7143788c-d20d-40ba-954f-04c823821300; _ym_uid=1654093697523257618; _gcl_au=1.1.1114733637.1676210476; _ym_d=1676210477; _cfuvid=yiInqdwIzAThtApU98Bh5p5G6blM8HRSrlmABSK0fys-1676739752094-0-604800000; VisitCount=15; SearchMode=1; platform=web; __cfruid=91ee46611745990c2a950bbc755e8c0c4c85df8a-1676739752; sid=eZApZh4JvW; __utmzzses=1; _gid=GA1.2.2054568514.1676739754; OptanonAlertBoxClosed=2023-02-18T17:02:34.115Z; _ym_isad=1; _ym_visorc=b; WebAbTesting=A_31-B_9-C_34-D_75-E_37-F_6-G_94-H_51-I_9-J_65-K_41-L_71-M_74-N_16-O_93-P_14-Q_20-R_31-S_51-T_73-U_61-V_28-W_43-X_4-Y_25-Z_3; cto_bundle=1kEo4V91JTJGbkE0V0tscHNwQW92QjlJZXBkV04yaVIxSlJPYjh6QU02JTJGOUolMkYwVDRHd1ZNU3pRWVpLMmxqRG9HN3BtS1VxQ3dLVU93a292NyUyQkJDdHpEMmpXR0ZhQjJTdk9OVExpYVNyYmhUUk5idkdFdjdkQWVwUnhiMlRsTVhSVGdVMjJmWlZwb0lFN3RYeUU3JTJCcFglMkZSRDhnalElM0QlM0Q; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdGFuZGFyZFVzZXIiOiIwIiwidW5pcXVlX25hbWUiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJzdWIiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImF0d3J0bWsiOiIxMmE5ZGViYi1hZmFlLTExZWQtOTYyZS01ZWFiMGJlMzk2Y2UiLCJ1c2VySWQiOiIyOTc4NzI2NyIsImVtYWlsIjoiY2hhbGxlbmdlcjkxNTFAZ21haWwuY29tIiwiYXVkIjoic2JBeXpZdFgramhlTDRpZlZXeTV0eU1PTFBKV0Jya2EiLCJleHAiOjE4MzQ1Mjc3NjksImlzcyI6ImF1dGgudHJlbmR5b2wuY29tIiwibmJmIjoxNjc2NzM5NzY5fQ.mJ_n0YbMOr_9vjJ6wZLzy8jasMnKXUma48QBaBgV4yE; UserInfo=%7B%22Gender%22%3A%221%22%7D; COOKIE_TY.Entrance=x=29787267&pp=GHGPiipiov3t4h/TdPy2qUp62Sw=&tx=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdGFuZGFyZFVzZXIiOiIwIiwidW5pcXVlX25hbWUiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJzdWIiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImF0d3J0bWsiOiIxMmE5ZGViYi1hZmFlLTExZWQtOTYyZS01ZWFiMGJlMzk2Y2UiLCJ1c2VySWQiOiIyOTc4NzI2NyIsImVtYWlsIjoiY2hhbGxlbmdlcjkxNTFAZ21haWwuY29tIiwiYXVkIjoic2JBeXpZdFgramhlTDRpZlZXeTV0eU1PTFBKV0Jya2EiLCJleHAiOjE4MzQ1Mjc3NjksImlzcyI6ImF1dGgudHJlbmR5b2wuY29tIiwibmJmIjoxNjc2NzM5NzY5fQ.mJ_n0YbMOr_9vjJ6wZLzy8jasMnKXUma48QBaBgV4yE&FirstName=atabek&LastName=iskenderov&Gender=1&Phone=553%2A%2A%2A%2A%2A82&UserName=atabek%20iskenderov&VisitorType=Elite&EmailSha255Hashed=4e29fd9e20bc37e58bb9cfa8e891dd5406da2df4e51c97bdbfe9286e224b53ce&EmailMd5Hashed=b12fcdd2a798b613a75bc9ce680da7ce&UserTypeStatus=Elite&UserId=29787267&Email=challenger9151%40gmail.com&RefreshToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzY4MjYxNjksInN1YiI6MX0.Lr6-kTi9nndUVHEYoaiRi6EH-WvzJDu9LWgwEHmataY&HasDeviceToken=False&HasSavedCreditCard=False&MarketingEmailsAuthorized=False; COOKIE_UserTypeStatus=x=Elite&pp=tfTrTr1neb7rJCxg6kx1jIH+m3M=&tx=tfTrTr1neb7rJCxg6kx1jIH+m3M=&toBeInfluencer=False; VisitorTypeStatus=Elite; COOKIE_TY.FirstVisit=x=TY.FrstVst&pp=1EE6aLrZvguCLIVZ0ukD3Q574BY=&tx=1EE6aLrZvguCLIVZ0ukD3Q574BY=&; COOKIE_TY.UserAlreadyLogged=x=1&pp=gmzZ7qH19gWXfdueTp3NLhm5Eyg=&tx=gmzZ7qH19gWXfdueTp3NLhm5Eyg=&; __dtxPOUD=x=Female&pp=Uwo3ksNeOxJP+gL9E8t2Ffx6ByA=&tx=Uwo3ksNeOxJP+gL9E8t2Ffx6ByA=&; _dc_gtm_UA-13174585-1=1; access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdGFuZGFyZFVzZXIiOiIwIiwidW5pcXVlX25hbWUiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJzdWIiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImF0d3J0bWsiOiIzMTdmMzczZi1hZmFlLTExZWQtYmM0Ny01MjE3MDhhNDRmYjYiLCJ1c2VySWQiOiIyOTc4NzI2NyIsImVtYWlsIjoiY2hhbGxlbmdlcjkxNTFAZ21haWwuY29tIiwiYXVkIjoic2JBeXpZdFgramhlTDRpZlZXeTV0eU1PTFBKV0Jya2EiLCJleHAiOjE4MzQ1Mjc4MjAsImlzcyI6ImF1dGgudHJlbmR5b2wuY29tIiwibmJmIjoxNjc2NzM5ODIwfQ.CmNFpH1-UXsXJ8qTjL81oFOoIV4HgGjXJiV0meCe1fI; _ga_1=GS1.1.1676739756.4.1.1676739822.0.0.0; _ga=GA1.2.735037227.1654093697; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+18+2023+20%3A03%3A46+GMT%2B0300+(GMT%2B03%3A00)&version=6.30.0&isIABGlobal=false&hosts=&genVendors=V67%3A0%2CV1%3A0%2C&consentId=ec001d60-3f55-43c2-8563-ca7fd657e862&interactionCount=4&landingPath=NotLandingPage&groups=C0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0001%3A1%2CC0007%3A1&AwaitingReconsent=false&geolocation=TR%3B06; _ga_8F2NHTRF7T=GS1.1.1676739753.21.1.1676739826.47.0.0',
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
    # 'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdGFuZGFyZFVzZXIiOiIwIiwidW5pcXVlX25hbWUiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJzdWIiOiJjaGFsbGVuZ2VyOTE1MUBnbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImF0d3J0bWsiOiI1YjU2ZTRiMy1hZmFmLTExZWQtYWE4MC00MmExMTM0ZTU4ZDciLCJ1c2VySWQiOiIyOTc4NzI2NyIsImVtYWlsIjoiY2hhbGxlbmdlcjkxNTFAZ21haWwuY29tIiwiYXVkIjoic2JBeXpZdFgramhlTDRpZlZXeTV0eU1PTFBKV0Jya2EiLCJleHAiOjE4MzQ1MjgzMjAsImlzcyI6ImF1dGgudHJlbmR5b2wuY29tIiwibmJmIjoxNjc2NzQwMzIwfQ.3U7sURSfGiIjpjG0omRb9E8vxTiuAqt4nXK4ONCrFIg',
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
