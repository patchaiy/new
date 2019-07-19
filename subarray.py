def n(l):
        ni1=1
        for x in range(0,len(l)-1):
                if l[x]!=l[x+1]:
                        ni1=ni1+1
                else:
                    break
        return ni1
numi=int(input())
l=list(map(int,input().split()))
for x in range(0,len(l)):
        if l[x]>0:
                l[x]=1
        else:
             l[x]=0
nn2=""
for x in range(0,len(l)):
        k=l[x::]
        nn2=nn2+str(n(k))+" "
print(nn2.strip())
