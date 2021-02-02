import pandas as pd
import re
import numpy as np
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
# %matplotlib inline
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

url = 'http://fund.eastmoney.com/js/fundcode_search.js'
r = requests.get(url)
pb = re.compile(r'"(\d*?)","(.*?)","(.*?)","(.*?)","(.*?)"')
dataset = re.findall(pb,r.text)

fund_name,fund_no,fund_type = [],[],[]
for data in dataset:
    fund_no.append(data[0])
    fund_name.append(data[2])
    fund_type.append(data[3])
# print(fund_no)
# print(fund_name)
# print(fund_type)
# print(len(fund_type),len(fund_no),len(fund_name))
fund_info = pd.DataFrame({
    '基金代码': fund_no,
    '基金名称': fund_name,
    '基金类型': fund_type
})
# print(fund_info)
# writer = pd.ExcelWriter(
#     r'D:\OneDrive - whut.edu.cn\脚本备份\MyPythonWork\天天基金数据导出.xlsx')
# fund_info.to_excel(writer,sheet_name='天天基金信息',index = 0)
# writer.save()
# writer.close()

# group_num = fund_info.groupby('类型').agg(fund_num= ('类型','count')).sort_values(by='fund_num',ascending = flase).reset_index('类型')
plt.style.use('ggplot')
fig = plt.figure(figsize=(20.8))
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
# plt.bar(x = '类型', height='基金数量',data = group_num)
# for a,b in zip(range(len(group_num.))),group_num.fund_num):
#     plt.text(a,b,b,ha='center',va='bottom',fontsize=16)
# plt.title('各类基金数量',fontdict={'fontsize':20})
