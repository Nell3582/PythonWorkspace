import appex
import clipboard
import console
import requests
import json


text = pyperclip.paste()

class dd:
    def req(self):
        #把第二步中获取到的 timestamp和sign拼接到URL中
        url = ('https://oapi.dingtalk.com/robot/send?access_token=9d35a417fd13301e046c31eb6deb29c47b769531a1e9d5e73b8a37d56dd1f2c1&timestamp=1612263003859&sign=B5Q86Vohcwn5rWKcItthGWGkY4kWudr1CyW0vd7kakk%3D')
        h = {
            'content-type':
            'application/json',
            'User-Agent':
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }
        #d里面的at参数是需要at的人参数，只有at的人存在这个参数里面才会@成功
        d = json.dumps({
            "msgtype": "text",
            "text": {
                "content": text
            },
            # "at": {
            #     "atMobiles": ["15207163636"],
            #     "isAtAll": "false"
            # }
        })
        req = requests.post(url, data=d, headers=h)
        data = req.json()
        if data.error_code == 0 and data.errmsg == 'ok':
            print('发送成功,请到客户端查看相关信息')
        print(req.text)


# def main():
#     text = appex.get_text()
#     if curl:
#         url, body, headers, method = parse_curl(curl)
#     else:
#         path = appex.get_file_path()
#         url, body, headers, method = parse(path)
# if __name__ == '__main__':
#     dd().req()

text = appex.get_text()
console.hud_alert('已发送,请查收')

if __name__ == '__main__':
    if appex.is_running_extension():
        dd().req()
    else:
        print('请设置为 Share Extension 脚本后使用。')
