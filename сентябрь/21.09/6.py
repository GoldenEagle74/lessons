  while True:
	a = int(input('Введите сумму: '))
	if a == 0: break
	while a%2==0:
		a//=2
	a -= a*0.15
	print('К оплате: {}'.format(a))
