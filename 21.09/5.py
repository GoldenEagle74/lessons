while True:
	a = int(input('Введите стоимость товара: '))
	if a == 0: break
	b = int(input('Введите скидку на товар: '))
	print('Стоимость:',a-a*(b/100))
