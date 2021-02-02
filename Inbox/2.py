import json
import pdb
# x = int(input('请输入您要计算的数字'))

# if x > 1:
#   y = 3*x-5
# elif x < -1:
#   y = 5*x +3
# else:
#   y = x + 2

# print(f'您输入的数字为{x},相应计算结果为{y}')

input_data = str(input("请分别按顺序输入三角形的长宽高，请使用逗号或空格隔开"))

def split_data():
  try:
    data = input_data.split(",")
    pdb.set_trace
    if len(data) == 3:
      print("数据格式校验错误，请检查是否按照要求正确输入")
    else:
      group = []
      for i in data:
        num = int(i)
        group = group.append(num)
        print(f'您输入的第{i}个数字为{num},请核对是否正确/n')
        a = group[0]
        b = group[1]
        c = group[2]
        return a, b, c
  except Exception as e:
    raise e

def panduan(a,b,c):
  try:
    if a+b>c and a+c>b and b+c>a:
      L = a + b + c
      S = a*b*0.5
      print(f"该三角形的周长为{L},面积为{S}")
    else:
      print('不能构成三角形')
  except Exception as e:
    raise e


if __name__ == '__main__':
  split_data()
  panduan(a,b,c)


