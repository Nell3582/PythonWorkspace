# 练习题1
# 根据用于指定月份，打印该月份所属的季节。
# 提示: 3,4,5 春季 6,7,8 夏季 9,10,11 秋季 12, 1, 2 冬季


# dic = {'chun':[3,4,5],'xia':[6,7,8],'dong':[12,1,2],'qiu':[9,10,11]}
# dic2 = {(3,4,5):'chun',(6,7,8):'xia',(9,10,11):'qiu',(12,1,2):'dong'}
# month = [8,12,18,0,5,9]

# for i in month:
# 	if i in range(1,13):
# 		for key,value in dic2.items():
# 			if i in key:
# 				result = dic2.get(key)
# 				print(f"{i}月份对应的季节为{result}")
# 	else:
# 		print(f'你输入的月份为{i},请确认该月份数值正确')

# 练习2 
# names = ['fentiao','fendai','fensi','fish']
# print('I have {},{},{} and {}'.format(names[0],names[1],names[2],names[3]))
# print(f'I have {names[0]},{names[1]},{names[2]} and {names[3]}')
# print('I have ' + ','.join(names[:-1]) + ' and ' + names[-1])


users = ['root','westos']
passwds = ['123','456']
dic = dict(zip(users,passwds))
# print(dic)
# userslist = ['kkkk','wwww','root','admin','kang']
# a = input('请输入您的用户名')
# b = input('请输入您的密码')
def input_info():
	a = input('请输入您的用户名')
	b = input('请输入您的密码')
	return a,b

def login(user,paswd):
	try:
		print(dic.keys())
		print(user)
		if user in dic.keys():
			if paswd == dic.get(user):
				print('登陆成功')
				result = 'success'
				return result
			else:
				for i in range(2):
					i += 1
					print('登陆失败，当前密码与账户密码不一致，请重试,您还有{}次机会'.format(3-i))
					input_info()
		else:
			print('您不具有本公司管理员权限，请获取权限后在登陆')
	except Exception as e:
		raise e



# 练习3
from faker import Faker #用于模拟生成数据
faker = Faker("zh_CN")
userlist = []
joblist = []
for i in range(10):
     userlist.append(faker.name())
     joblist.append(faker.job())
user_dict = dict(zip(userlist,joblist))
# print(user_dict)

def info_manage(status):
	if status == 'success':
		while True:
			a = int(input('请输入您想要进行的操作：\n 1.添加会员信息\n 2.删除会员信息\n 3.查看会员信息\n 4.退出\n'))
			if a == 1:
				new_user_name = input('请输入您想要添加的会员姓名')
				new_user_job = input('请输入您想要添加的会员工作信息')
				user_dict[new_user_name] = new_user_job
				print(f'{new_user_name}会员信息已添加，现有会员列表为：')
				info_found()
			if a ==2:
				del_name = input('请输入您想要删除的会员信息')
				if del_name in user_dict.keys():
					del user_dict[del_name]
					print(f'{del_name}身份信息已删除，现有会员信息列表为;')
					info_found()
				else:
					print("不存在该会员身份信息，请键入有效的会员姓名")
			if a == 3:
				info_found()
			if a == 4:
				print('已退出系统')
				# break
				return

def info_found():
	for k, v in user_dict.items():
		print(k + ':' + v)


f = input_info()
user = f[0]
paswd = f[1]

status = login(user,paswd)

print(status)

login
info_manage(status)












