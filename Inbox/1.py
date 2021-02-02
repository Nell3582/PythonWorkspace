# import json
# import pdb
# # x = int(input('请输入您要计算的数字'))

# # if x > 1:
# #   y = 3*x-5
# # elif x < -1:
# #   y = 5*x +3
# # else:
# DATA=[]
# #   y = x + 2

# # print(f'您输入的数字为{x},相应计算结果为{y}')

# input_data = input("请分别按顺序输入三角形的长宽高，请使用逗号或空格隔开")
# # input_data = '5 6 1'
# print(input_data, type(input_data))

# def split_data(self):
#   try:
#     data = input_data.split(" ") #python内建的split()函数只能使用单个分隔符
#     print(data)
#     pdb.set_trace
#     if len(data) != 3:
#       print("数据格式校验错误，请检查是否按照要求正确输入")
#     else:
#       group = []
#       k = 1
#       for i in data:
#         num = int(i)
#         group.append(num)
#         print(f'您输入的第{k}个数字为{num},请核对是否正确/n')
#         k +=1
#       a = group[0]
#       b = group[1]
#       c = group[2]
#       return a,b,c
#   except Exception as e:
#     raise e
# # print(a,b,c)
# def panduan(a,b,c):
#   try:
#     if a+b>c and a+c>b and b+c>a:
#       L = a + b + c
#       S = a*b*0.5 #计算方法不对但是主要是理解这个过程就行
#       print(f"该三角形的周长为{L},面积为{S}")
#     else:
#       print('不能构成三角形')
#   except Exception as e:
#     raise e

# if __name__ == '__main__':
#   # w = split_data(input_data)
#   # print(panduan(w[0],w[1],w[2]))
#   a,b,c = split_data(input_data)
#   print(panduan(a,b,c))



row = 5
#row =  int(input("请输入您想排列的行数"))
for i in range(row+1):
  # print('*' * i, ' ' * (row-i)) #图案一
  print(' ' * (row-i),'*' * i)#图案二

