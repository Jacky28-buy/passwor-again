x = 3
password = 'kkbao'


while True:
	pw = input('请输入密码')
	x = x - 1
	if pw != password:
		if x != 0:
			print('密码错误！还有', x , '次机会')
		else:
			print('没机会了')
			break
	if pw == password:
		print('密码正确')
		break
