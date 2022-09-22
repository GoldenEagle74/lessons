a = input()
n=['-' , ' (' , ') ']
for i in range(len(n)):
	if n[i] in a:
		a=a.replace(n[i],'')
print(a)
