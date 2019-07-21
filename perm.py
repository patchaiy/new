ni=int(input())
li=list(map(int,input().split()))
ss,li1=0,[]
li2=[x for x in range(1,ni+1)]
for i in li:
  if i in li2:
    li2.remove(i)
kh=0
for i in range(0,ni-1):
  p=li[i]
  for j in range(i+1,ni):
    if(p==li[j]):
      if(p<li2[kh]):
        li[j]=li2[kh]
        ss+=1
      else:
        li[i]=li2[kh]
        ss+=1
      kh+=1
print(ss)
print(*li)
