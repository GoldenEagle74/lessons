while True:
	a = input()
	if a == 'game':
		print('Угадай число')
		for i in range(3):
			try: j = int(input('Введите число: '))
			except: exit()
			if j == 5:
				print('Вы выиграли билет на концерт!')
				break
			else:
				if i==0: print('Неправильный ответ, осталось 2 попытки')
				if i==1: print('Неправильный ответ, осталась 1 попытка')
				if i==2: print('Неправильный ответ, игра окончена')
				
	elif a == 'off': break
