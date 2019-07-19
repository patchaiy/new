n=int(input())
a1=list(map(int,input().split()))
p=[]
q=[]
for i in range(len(a1)):
	if i%2==0:
		p.append(a1[i])
	else:
		q.append(a1[i])
s=sum(p)
r=sum(q)
if(s>r):
	print(s)
else:
	print(r)
