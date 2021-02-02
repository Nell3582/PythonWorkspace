import requests
import time
from datetime import datetime

cookies = {
    'PHPSESSID': 'hf0p8uu9sh16dhajh65sfjjf93',
}

headers = {
    'Host': 'bububao.duoshoutuan.com',
    'tokenstr': '3405A7CD88772724517FBB66B525244G1611012141',
    'accept': '*/*',
    'version': '10',
    'idfa': '00000000-0000-0000-0000-000000000000',
    'accept-language': 'zh-cn',
    'platform': '2',
    'imei': '8A41B05E-09FF-4917-AFD3-3B72A5941671',
    'user-agent': 'BBB/132 CFNetwork/1209 Darwin/20.2.0',
    'store': 'appstore',
}




def getUserInfo():
    r = requests.post('https://bububao.duoshoutuan.com/user/profile', headers=headers, cookies=cookies)
    data = r.json()
    username = data['username']
    jinbi = data['jinbi']
    leiji_jinbi = data['leiji_jinbi']
    money = data['money']
    try:
        if r.status_code == 200 and data['uid'] == '525244':
            print('账号登陆成功')
            print(f'当前步步宝账号: {username}\n当前账号金币: {jinbi}\n累计获得金币数: {leiji_jinbi}\n可体现金额: {money}元')
    except:
        print(f'An exception occurred:\n{data}')
# getUserInfo()

def signIn():
    url = 'https://bububao.duoshoutuan.com/user/sign'
    r = requests.post(url,headers=headers, cookies=cookies)
    data = r.json()
    jinbi = data['jinbi']
    if r.status_code == 200 and data['code'] == 1:
        signInstr = data['nonce_str']
        print(data['msg'])
        return signInstr


def signDouble():
    url = 'https://bububao.duoshoutuan.com/you/callback'
    r = requests.post(url,headers=headers, cookies=cookies)
    data = r.json()

