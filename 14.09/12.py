a = input()
ind1 = a.find('&nbsp;')
str1 = ''
for i in range(ind1-1, 0, -1):
	if a[i].isdigit():
		str1 += a[i]
	else:
		break
str1 = str1[::-1]
ind2 = a.rfind('&nbsp;')
str2 = ''
for i in range(ind2-1, ind1, -1):
	if a[i].isdigit():
		str2 += a[i]
	else:
		break
str2 = str2[::-1]
str3 = str1 + str2
print(int(str3) + 1)
