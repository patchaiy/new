ni=int(input())
a1=list(map(int,input().split()))
a1=[bin(i) for i in a1]
a1.sort(reverse=True)
a1=[int(y,2) for y in a1]
for i in range(0,ni):
 print(a1[i])
