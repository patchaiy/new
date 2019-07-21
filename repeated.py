di=int(input())
ki=0
lst=input().split()
lst=list(map(int,lst))
new=[]
for i in range(0,di):
    if((lst.count(lst[i]))>=2):
      if lst[i] not in new:
        new.append(lst[i])
        ki=1
if(ki==0):
  print("unique")
else:
  for i in range(0,di):
    print(min(new),end=" ")
    new.remove(min(new))
