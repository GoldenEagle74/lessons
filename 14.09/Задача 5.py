a = int(input())
b = a
sm = 0
while b != 0:
	sm+=b%10
	b//=10
print((a%10)%2==0 and sm%3==0)