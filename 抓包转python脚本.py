'''
自助选取文件,并转成自动化python脚本,适用于Charles抓包保存的chlsj格式文件,后续支持har文件,处理后文件自动复制到剪切板,可直接复制到编辑器中使用
'''
import json
import pyperclip
from tkinter import filedialog
from tkinter import messagebox

Fpath = filedialog.askopenfilename()
fobj = open(Fpath, 'r')
f = fobj.readlines()
lst = json.loads(f[0])

def get_Info(num,**kwargs):
    item = kwargs
    method = item['method'].lower()
    request = item['request']
    d = item['request']['header']
    scheme,host,path = item['scheme'],item['host'],item['path']
    url = scheme + '://' + host + path
    headers = {i['name']: i['value'] for i in d['headers']}
    if request.get('body', ' ') != ' ':
        body = request.get('body')['text']
    else:
        body = ' '
    js = f'''

def function{num}():
  url = {json.dumps(url)};
  body = {json.dumps(body)};
  headers = {json.dumps(headers, indent=4)};
  try:
    response = requests.{method}(url, data=body, headers=headers);
    data = response.json()
    print(data)

  except Exception as e:
    print(f'An exception occurred')
    raise
    
'''
    return js


js = ''
num = 0
for item in lst:
    result = get_Info(num,**item)
    js += result
    num += 1

pyperclip.copy(js)
messagebox.showinfo("任务完成", "内容已复制到剪切板,请直接到所需处粘贴")
