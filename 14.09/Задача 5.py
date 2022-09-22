a = int(input())
sm = 0
while a != 0:
	sm+=a%10
	a//=10
if (a%10)%2==0 and sm%2==0: print(True)
else: print(False)
