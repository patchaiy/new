import math
p1,q=map(int,input().split())
n=[]
v=list(map(int,input().split()))
for i in range(0,q):
        a,b=map(int,input().split())
        n.append([a,b])
for i in n:
        x=i[0]-1
        y=i[1]-1
        print(math.gcd(v[x],v[y]))
