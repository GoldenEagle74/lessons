a = input()
n='=?*^$№@_'
b=[]
for i in a:
	if i in n:
		b.append(i)
if len(b)!=0: print(''.join(b))	
