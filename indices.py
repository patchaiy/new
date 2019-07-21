pi=int(input())
val=list(map(int,input().split()))
x=0
for i in range(pi):
    if sum(val[:i])==sum(val[i+1:]):
        x=x+1
if x>0:
    print("yes")
else:
    print("no")
