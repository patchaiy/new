n3=int(input())
lis3=list(map(int,input().split()))
choco1=1
count=0
if lis3[0]>lis3[1]:
    choco1=choco1+1
    count=count+choco1
else:
    count=choco1
for i in range(1,len(lis3)):
    if lis3[i]>lis3[i-1]:
        choco1=choco1+1
        count=count+choco1
    else:
        choco1=1
        count=count+choco1
print(count)
