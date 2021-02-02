# import appex
# import clipboard
# import console
# import re
# import shlex
import requests
import json
import pyperclip



# function tgBotNotify(text, desp) {
#   return  new Promise(resolve => {
#     if (TG_BOT_TOKEN && TG_USER_ID) {
#       const options = {
#         url: `https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage`,
#         body: `chat_id=${TG_USER_ID}&text=${text}\n\n${desp}&disable_web_page_preview=true`,
#         headers: {
#           'Content-Type': 'application/x-www-form-urlencoded'
#         }
#       }
#       if (process.env.TG_PROXY_HOST && process.env.TG_PROXY_PORT) {
#         const tunnel = require("tunnel");
#         const agent = {
#           https: tunnel.httpsOverHttp({
#             proxy: {
#               host: process.env.TG_PROXY_HOST,
#               port: process.env.TG_PROXY_PORT * 1
#             }
#           })
#         }
#         Object.assign(options, { agent })
#       }
#       $.post(options, (err, resp, data) => {
#         try {
#           if (err) {
#             console.log('telegram发送通知消息失败！！\n')
#             console.log(err);
#           } else {
#             data = JSON.parse(data);
#             if (data.ok) {
#               console.log('Telegram发送通知消息完成。\n')
#             } else if (data.error_code === 400) {
#               console.log('请主动给bot发送一条消息并检查接收用户ID是否正确。\n')
#             } else if (data.error_code === 401){
#               console.log('Telegram bot token 填写错误。\n')
#             }
#           }
#         } catch (e) {
#           $.logErr(e, resp);
#         } finally {
#           resolve(data);
#         }
#       })
#     } else {
#       console.log('您未提供telegram机器人推送所需的TG_BOT_TOKEN和TG_USER_ID，取消telegram推送消息通知\n');
#       resolve()
#     }
#   })
# }

# TG_BOT_TOKEN = '1572513125:AAHDokotZU8dQquPPeg1BJH27oeap0hhDCw'
# TG_USER_ID = '995328749'
# # text = pyperclip.paste()
TG_BOT_TOKEN ='1347008371:AAE9lvHp5yB0jPVtuhL20G13AlQ5Xbnen6E';
# //此处填你接收通知消息的telegram用户的id，例如：129xxx206
# //注：此处设置github action用户填写到Settings-Secrets里面(Name输入TG_USER_ID)
TG_USER_ID = '995328749';
text = 'my'
def tgBotNotify(text):
    url = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage'
    body = f'/chat_id={TG_USER_ID}&text={text}&disable_web_page_preview=true'
    #         url: `https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage`,
    #         body: `chat_id=${TG_USER_ID}&text=${text}\n\n${desp}&disable_web_page_preview=true`,
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(url, data=body, headers=headers);
        data = response.json()
        print(data)
    except Exception as e:
        print(f'An exception occurred')
        raise


tgBotNotify(text)
