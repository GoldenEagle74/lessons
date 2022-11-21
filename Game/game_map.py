from os import system
from time import sleep


def map_image():
	img = [['.' for x in range(61)] for y in range(29)]
	# Первые и 3 круги
	x1 = {y:[x for x in range(9,17)]+[x for x in range(27,35)]+[x for x in range(45,53)] for y in range(18,21,2)}
	x2 = {19:[x for x in range(8,54)]}
	# 4 и 5 круги
	x3 = {11:[x for x in range(26,54)]}
	x4 = {y:[x for x in range(45,53)] + [x for x in range(27,35)]for y in range(10,13,2)}
	# 6 круг
	x5 = {26:[x for x in range(44,54)]}
	x6 = {y:[x for x in range(45,53)] for y in range(25,28,2)}
	# Вертикальная линия
	x7 = {y:[49] for y in range(13,18)} | {y:[49] for y in range(21,25)}
	d = x1|x2|x3|x4|x5|x6|x7
	for y in d:
		for x in d[y]:
			if x in range(0,61): img[y][x] = '='
	return img
	

def image(img, d, refresh):
	if refresh: img = map_image()
	for y in d:
		for x in d[y]:
			if x in range(0,61): img[y][x] = '*'
	return img

#========Указание расположения пикселей========	

def char(location):
	locations = {
		1:[0,0],
		2:[18,0],
		3:[19 * 2 - 1, 0],
		4:[19 * 2 -1, 8],
		5:[18, 8],
		6:[19 * 2 - 1, - 7]
	}
	img = map_image()
	a, b = locations[location]
	#==============Head==============
	x1 = {y - b:[x for x in range(11 + a,14 + a)] for y in range(10,13,2)}
	x2 = {11 - b:[10 + a,14 + a]}
	#==============Arms==============
	x3 = {13 - b:[x for x in range(10 + a, 15 + a)]}
	x4 = {y - b:[9 + a,12 + a,14 + a +(y-14)] for y in range(14,16)}
	x5 = {16 - b:[12 + a]}
	#==============Legs==============
	x6 = {17 - b:[x for x in range(11 + a,14 + a)]}
	x7 = {y - b:[11 + a -(y-18),14 + a] for y in range(18,20)}
	
	system('clear')
	for y in image(img, x1|x2|x3|x4|x5|x6|x7, True): print(''.join(y))
	sleep(0.5)
	system('clear')
	
	#==============Head==============
	x1 = {y - b:[x for x in range(11 + a,14 + a)] for y in range(10,13,2)}
	x2 = {11 - b:[10 + a,14 + a]}
	#==============Arms==============
	x3 = {13 - b:[x for x in range(10 + a,15 + a)]}
	x4 = {y - b:[9 + a +(y-14),12 + a,14 + a] for y in range(14,16)}
	x5 = {16 - b:[12 + a]}
	#==============Legs==============
	x6 = {17 - b:[x for x in range(11 + a,14 + a)]}
	x7 = {y - b:[11 + a,14 + a+(y-18)] for y in range(18,20)}
	
	for y in image(img, x1|x2|x3|x4|x5|x6|x7, True): print(''.join(y))
	sleep(0.5)
	system('clear')
