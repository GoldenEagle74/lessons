n = []
while True:
	a = input()
	if a == '0': break
	if a in n: print('Эта игра уже записана')
	else: n.append(a)
n.sort()
