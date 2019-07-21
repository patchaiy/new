t3,t4,t5,t6=map(int,input().split())
li3=list(map(int,input().split()))
xii=[]
for i in range(0,len(li3)):
    for j in range(i,len(li3)):
        for k in range(j,len(li3)):
            xii.append(t4*li3[i]+t5*li3[j]+t6*li3[k])
print(max(xii))
