n=int(input())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
for i in range(len(lst)):
  print(lst[i],end="")
