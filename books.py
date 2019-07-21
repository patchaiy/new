import sys,string, math, itertools

nbi,ks = input().split()
nbi,ks = int(nbi),int(ks)
L = [ int(x) for x in input().split()]
#print(nbi,ks, L)
for i in range(0,nbi) :
    if (86400-L[i]) >= ks :
        print(i+1)
        sys.exit()
    ks -= (86400-L[i])
