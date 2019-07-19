from itertools import combinations
Sim,u=map(int,input().split())
li=len(str(Sim))
lst=list(combinations(str(Sim),li-u))
lst=sorted(lst)
print(*lst[0],sep='')
