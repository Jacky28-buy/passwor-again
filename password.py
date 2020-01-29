x = 3



while True:
	pw = input('请输入密码')
	x = x - 1
	if pw != 'kkbao':
		if x != 0:
			print('密码错误！还有', x , '次机会')
		if x == 0:
			print('没机会了')
			break
	if pw == 'kkbao':
		print('密码正确')
		break
