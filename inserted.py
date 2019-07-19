m,n=map(str,input().split())
t=0
if len(m)>len(n):
  m,n=n,m
r=0
while r<len(m):
  t+=(ord(n[r])-ord(m[r]))
  r+=1
for r in range(r,len(n)):
  t+=ord(n[r])-ord('a')+1
print(t)
