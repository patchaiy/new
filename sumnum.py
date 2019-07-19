ai=int(input())
bi=list(map(int,input().split()))
c=0
for m in range(0,ai):
	for p in range(0,m):
		if bi[p]<bi[m]:
			c=c+bi[p]
print(c)
