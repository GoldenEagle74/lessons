s = input()
x, y, z = s.split(' ')
x, y, z = int(x), int(y), int(z)
if x < y and y < z:
	print("Акция!")
	s=(x+y+z)//2
elif x > y and y > z:
	print("Акция!")
	s=(x+y+z)//3
else: s=(x+y+z)
print("К оплате: {0}".format(s))
