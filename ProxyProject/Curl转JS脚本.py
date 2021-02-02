import zipfile
import json
from urllib3.filepost import encode_multipart_formdata as emf
import argparse
import re
import shlex
from tkinter import messagebox
import pyperclip


def parse_curl(curl_command):
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('url')
    parser.add_argument('-d', '--data')
    parser.add_argument('--data-raw', default='')
    parser.add_argument('-b', '--data-binary', default=None)
    parser.add_argument('-X', default='')
    parser.add_argument('-k', action="store_true")
    parser.add_argument('--insecure', action='store_true')

    method = "get"
    parser.add_argument('-L', action="store_true")
    parser.add_argument('-H', '--header', action='append', default=[])
    parser.add_argument('--compressed', action='store_true')
    tokens = shlex.split(curl_command)
    parsed_args = parser.parse_args(tokens)

    post_data = parsed_args.data or parsed_args.data_binary or parsed_args.data_raw
    if post_data:
        method = 'post'

    if parsed_args.X:
        method = parsed_args.X.lower()
    url = parsed_args.url
    body = post_data if post_data else ''
    headers = {}
    for curl_header in parsed_args.header:
        if curl_header.startswith(':'):
            occurrence = [m.start() for m in re.finditer(':', curl_header)]
            header_key, header_value = curl_header[:occurrence[
                1]], curl_header[occurrence[1] + 1:]
        else:
            header_key, header_value = curl_header.split(":", 1)

        headers[header_key] = header_value.strip()

    return url, body, headers, method


curl = pyperclip.paste()
if curl[0:4] == 'curl':
    url, body, headers, method = parse_curl(curl)
else:
    messagebox.showinfo("任务失败", "请检查剪切板第一条是标准的curl链接")

js = f'''
function callBack() {{
return new Promise((resolve, reject) => {{
  let callback ={{
    url = {json.dumps(url)};
    body = {json.dumps(body)};
    headers = {json.dumps(headers, indent=4)};
}}
   $.{method}(callback,async(error, response, data) =>{{
    const back = JSON.parse(data)
    $.log('🔔任务开始')
    if(back.code == 1) {{
        $.log('🎉領取助力視頻獎勵成功,1s後查詢下一次助力視頻狀態')
        await $.wait(1000)
        await helpStatus()
        }}else{{
        $.log('⚠️助力視頻獎勵失敗:'+back.msg+'')
        }}
        resolve()
    }})
   }})
  }} 

  '''
  
pyperclip.copy(js)
messagebox.showinfo("任务完成", "内容已复制到剪切板,请直接到所需处粘贴")
# if __name__ == '__main__':
#     main()


  