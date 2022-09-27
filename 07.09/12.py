n = []
for i in range(5): n.append(float(input()))
a = n[0]*n[1]
b = a/n[2]*(1+n[4]/100)
c = round(b/n[3]+1)
print(round(a,2),round(b,2),c,round(c*n[3]-b,2),sep='\n')
