"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""
n, l = set(), set()
a = 0
for i in range(int(input())):
	if i != a: continue
	b = int(input())
	a += b
	m = set()
	for j in range(b):
		if len(n) == 0: n.add(input())
		else: m.add(input())
	n |= m
	if len(n) >= 2: l &= m
	else: l = m & n
print(len(n),str(list(n)).replace("'",""),sep = ' - ')
print(len(l),str(list(l)).replace("'",""),sep = ' - ')
