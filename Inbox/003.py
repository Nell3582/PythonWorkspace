import requests
import json
import time
# from datetime import datetime
# import time

# # t = time.time()
# # timestamp = format(t, '.0f')
# # host_api = 'https://kandian.youth.cn/n?timestamp='
# # signature = 'G5p4oJlXwm83BNKd2EvzMkp6qf7mebxZM7keny6aAROLjV9YzD'
# # url = host_api + timestamp + '&signature=' + signature + '&native=1&device_type=iphone&app_version=1.8.2&from=home'
# # r = requests.get(url, headers=headers, cookies=cookies)
# # print(r.text)
with open('2.har', 'r') as readObj:
    harDirct = json.loads(readObj.read())
    requestList = harDirct['log']['entries']
    lst =[]
    for item in requestList:
        urlString = (item['request']['postData']['params'][0])
        lst.append(urlString)
    # print(len(lst))
    body_list = []

    for item in lst:
        data_dict = dict()
        # str = item['name'] + '=' + item['value']
        data_dict[item['name']] = item['value']
        body_list.append(data_dict)

print(body_list)
import requests
headers = {
    'Host': 'ios.baertt.com',
    'Accept': '*/*',
    'User-Agent': 'KDApp/1.8.2 (iPhone; iOS 14.3; Scale/2.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
}
for item in body_list:
    r = requests.post('https://ios.baertt.com/v5/article/complete.json', headers=headers, data=item)
    print(r.json())
    time.sleep(5)





# data = {
#   'p': '9NwGV8Ov71o=gW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_kF97hamPuz4ZZk3rmRrVU_m2Z51XN3szZYaCPxNG07BYjyjwYkBVGTfTGYPVecze9u-jGHCQmfvey4yZrPyKR-cA01PbV3h61GBiHFc-skGrpoDK0eliCfJPX7f9_IVT-MEKcW_xpZA4LYK-zPANFjqRCwIjF9EEH7Kj7IudQYQD2OtIaZ_4Q5iaJIQgZGbpyURKdxm82vJFjI7CttJ649cgA-Nl0bB65gb7GBt3nXFoBtmaK7UuNfut8jYjeiRHpyrtl9jfZ6UOlSXVtluYpTlQ0bJLV28TSq8u2KxLOXPkKPdpfQi6P0I0U3ikl3ZOfYtARC4NanqFbPgRpGtQ9xtUFy2DWoHmw_rqOK6CpvAnujlw_TRuUOCoSukZRm9LBuAVl3psFr-DySaQbrZD_GS4vKT3J-yQQ-o4GEyXLjGBtTBHvtLQGtJYeQ1cSWG7pq0sWISJY7QzdhfyNH6FqRrKM61kptNuxoRfCiczor78HUfLGFB11-EdM94HG3WxI2cgU9q2MC9VsYyJQHZ2zUqpsKEFX4RjFc3xL4HgfPoeNvdKXcsPqolVu9U0Ih_MRr_8iZGVzaCgy9Fgkz78UAGNMJ5BkRBhghN6lAWzESb7S4e-JKCcZWr9Ea1b-Vt5E-HP32jxfvxarkDiRqT6VOq0ZfQorRWbaWs39ULogWvvdBB2Htog-CkOJKlU3euRWw_R_rkBwfaRHvi49qaCFwLBupQQPguo_ILXRl14wBU72RbQJbTqUAVBzlI9qfS5gxVwiJfwMEpgYqllF7ulXBdRh85N0JDviTNc8OmlA0ir73O0kaxPPQ=='
# }

