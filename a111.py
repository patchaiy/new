    
Ni=int(input())
k=[]
for i in range(0,Ni):
   l=list(map(int,input().split()))
   k.append(l)
s=0
for i in range(0,Ni):
   for j in range(0,Ni):
      if i+j==Ni-1:
         s=s+k[i][j]
print(s)
