import random

# N = int(input("请输入产生的整数数量"))
# s = set()
# for i in range(N):
# 	s.add(random.randint(0,1000))
# print(len(s),sorted(s))
# print(s)
# print( s == sorted(s))


# import random
# # 先生成n个随机数
# # 有先选择集和
# s = set([])
# for i in range(int(input('N:'))):
#     s.add(random.randint(1,1000))
# print(sorted(s))


# words = 'To begin taking advantage of the various packages for extending Sublime’s functionality, you need to manually install the package manager called Package Control. Once you have it installed, you can use it to install, remove, and upgrade all other ST3 packages.'
# # words = input('请输入您要分析的')
# fg = ['.',',',':']
# for i in fg:
# 	word = words.replace(i,' ')

# word_list = word.split(' ')
# print(word_list)
# #方法一、对于重复元素后续还会打印出来，未达到去重的目的
# # for i  in word_list:
# # 	print(f'{i}:{word_list.count(i)}')
# word_dict = {}
# for word in word_list:
# 	word_dict[word] = word_list.count(word)

# # for k in word_dict: #正确写法1
# # 	print(k,word_dict.get(k))

# for k,v in word_dict.items(): #正确写法2
# 	print(f"{k} : {v}")

# for k,v in word_dict: #错误写法
# 	print(f"{k} : {v}")
data_list = []
for i in range(100):
	data_list.append(random.randint(1,100))
print(data_list)

data_list_d = []
data_list_l = []
for data in data_list:
	if data > 66:
		data_list_d.append(data)
	else:
		data_list_l.append(data)

# data_tup_d = tuple(data_list_d)
# data_tup_l = tuple(data_list_l)

# data = {}
# data[data_tup_d] = ''
# data[data_tup_l] = ''
# print(data)

l1 = [11,22,33]
l2 = [22,33,44]
l3 = set()

# for i in l1:
# 	for j in l2:
# 		if i == j:
# 			l3.append(j)
# print(l3)

# for i in l2:
# 	for j in l1:
# 		if i not in  l1:
# 			l3.add(i)
# print(l3)
a = 'mynameis'
b = list(a)
print(b)


