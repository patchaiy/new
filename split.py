tti,tt4=map(int,input().split())
li=list(map(int,input().split()))
if tt4==1:
  print(min(li))
elif tt4==2:
  print(max(li[0],li[tti-1]))
else:
  print(max(li))
