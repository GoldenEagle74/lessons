"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def imt(weight,height):
	return imtc(float(weight / (height * height)))
def imtc(index):
	if index < 18.5: return 'Недостаточный вес'
	elif index >= 18.5 and index < 25: return 'ИМТ в норме'
	elif index >= 25: return 'Избыточный вес'
print(imt(int(input('Введите свой вес: ')),int(input('Введите свой рост: '))))
	
