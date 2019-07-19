mi,ni=map(str,input().split())
t=0
if len(mi)>len(ni):
  mi,ni=ni,mi
r=0
while r<len(mi):
  t+=(ord(ni[r])-ord(mi[r]))
  r+=1
for r in range(r,len(ni)):
  t+=ord(ni[r])-ord('a')+1
print(t)
