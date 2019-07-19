abc=int(input())
ba1=0
le=[]
for abc in range(1,abc+1):
  le.append(abc)
for abc in range(len(le)):
  for abc in range(abc+1,len(le)):
    ba1+=1
print(ba1)
