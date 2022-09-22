a = int(input())
sm = 0
while a != 0:
	sm+=a%10
	a//=10
print((a%10)%2==0 and sm%3==0)
