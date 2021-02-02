import random

# N = int(input('请输入需要产生的整数'))
# int(data) = set()
# for i in range(N):
#     int(data).add(random.randint(1,1000))
# print(sorted(int(data)))

# --------------------------------------------------
'''
思考题1:
随机生成100个卡号
卡号以6102009开头，后面3位依次是(901,002,003,100),
2.生成关于银行卡号的字興，默认每个卡号的初始密码为" redhat";
3.输出卡号和密码信息，格式如下：
卡号
密码
6162009001
'''
# lst = []
# s = set()
# d = dict()
# for i in range(100):
#     key = format(random.randint(1,100), '0>3')
#     s.add('6102009001'+ key)
# print(s)

# for key in s:
#     d[key] = 'redhat'

# for k,v in d.items():
#     print(k,v)

# --------------------------------------------------
'''
思考题2:
模拟轮盘抽奖游戏
轮盘分为三部分：一等奖，二等奖和三等奖
轮盘转的时候是随机的，
如果范围在[0,0.08)之间，代表一等奖，
如果范围在[0.08,0.3)之间，代表2等奖
如果范围在[6,1.0)之间，代表3等奖，
模拟本次活动1000人加，模拟当他们玩完游戏后爾要准备各等级奖品的个数？
'''
# --------------------------------------------------
''' 简易版 '''
# lst = []
# for i in range(1000):
#     lst.append(random.random())
# # yd_lst, ed_lst,sd_lst = [],[],[]
# c1, c2, c3 = 0, 0, 0
# for int(data) in lst:
#     if int(data) >= 0 and int(data) < 0.08:
#         c1 += 1
#     elif int(data) >= 0.08 and int(data) < 0.3:
#         c2 += 1
#     else:
#         c3 += 1
# print('一等奖获得者有' + str(c1) + '名')
# print('二等奖获得者有' + str(c2) + '名')
# print('三等奖获得者有' + str(c3) + '名')

# --------------------------------------------------
''' 函数版 '''
# def gen_random(num):
#     """
#     docstring 这里也可以使用列表生成式 简化 lst = [random.random() for i in range(100)]
#     """
#     lst = []
#     for i in range(num):
#         key = random.random()
#         lst.append(key)
#         return lst

# def game_info(*args):
#     """
#     关于函数的使用仍然不是很熟悉,明天需要多加进行练习
#     """
#     c1, c2, c3 = 0, 0, 0
#     for data in args:
#         if int(data) >= 0 and int(data) < 0.08:
#             c1 += 1
#             return c1
#         elif int(data) >= 0.08 and int(data) < 0.3:
#             c2 += 1
#             return c2
#         else:
#             c3 += 1
#             return c3
# lst = gen_random(100)
# game = game_info(lst)
# print(game)

# def print_info():
#     for i in range(3):
#         print(f'{i+1}等奖获得者有{lst[i]}人')

# a = gen_random(1000)
# print(a)
# game_info(a)

# --------------------------------------------------
'''
1.查找列表li中的元素，移除每个元素的空格，
并找出以’c’或者’C’开头，并以’e’结尾的所有元素，
并添加到一个新列表中,最后循环打印这个新列表。
li = ['CoXie','bigBear','ckuajie','QQqun',456926667,'text ']
'''
li = ['CoXie', 'bigBear', 'ckuajie', 'QQqun', 456926667, 'text ','ctexte ','ctext ',' text e']
li2 = ["马化腾", "马云", "刘强东","coxie"]
# lst = []
# for i in li:
#     if isinstance(i,str):
#         lst.append(i.strip())
#     else:
#         lst.append(i)

# new_lst = []
# for data in lst:
#     if isinstance(data,int):
#         pass
#     elif (data[:1] == 'c' or data[:1] == 'C') and data[-1:] == 'e':
#         new_lst.append(data)

# for i, value in enumerate(new_lst):
#     i += 1
#     # print(i,value)
#     print(f'当前列表第{i}个元素是:{value}')

# for data in new_lst:
#     print(data)

'''
函数版
在初次写函数时有几个错误,记录一下:
1. 关于可变参数的问题 Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去 
在传送参数是勿忘记添加* 将列表转变为可变参数在传输进去
2. return 应写在循环完成后 最后return 结果 否则循环未完成就跳出循坏 类似与 pass break 的作用
3. 函数的并列关系需要关注
'''
def strip_kg(*args):
    """
    该函数用于去除单词的首尾空格
    """
    lst = []
    for i in args:
        if isinstance(i,str):
            lst.append(i.strip())
        else:
            lst.append(i)
    return lst

def find_info(*args):
    """
    docstring
    """
    new_lst = []
    for data in args:
        if isinstance(data,str) and (data[:1] == 'c' or data[:1] == 'C') and data[-1:] == 'e':
            new_lst.append(data)
        else:
            pass
    return new_lst


def print_info(*args):
    """
    docstring
    """
    lst = []
    for i, value in enumerate(args):
        lst.append(f'当前列表第{i+1}个元素是:{value}')

    return lst

a = strip_kg(*li2)
b = find_info(*a)
c = print_info(*b)
# print(a)
# print(b)
print(c)



# --------------------------------------------------
'''
2.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
    敏感词列表 li = ["马化腾","马云",”刘强东”,”coxie”]
    则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；
    如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
3. 现有列表: bigbear = ['bigbear','boy',3,'SingleDog']
	利用两种方法，将列表的 3 换成23
	利用两种方法，将列表的 bigbear 变成大写
'''
li2 = ["马化腾", "马云", "刘强东", "coxie"]
import re
word = input('请输入您想评论的内容')
lst = []
for data in li2:
    word = re.sub(data, '***' ,word)
lst.append(word)
print(lst)


# --------------------------------------------------

'''
1.如：content = input(‘请输入内容:’)  # 如用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。

2.利用下划线将列表的每一个元素拼接成字符串，li = "alexericrain"
	li=['a','l','e','x','e','r','i','c','r','a','i','n']
'''
import re
content = input('请输入内容')
# lst = re.findall(r'\d+',content)
