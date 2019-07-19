st,st2=input().split()
cost_diff=abs(len(st)-len(st2))
for i in range(len(st)):
    if len(st2)==1 and st2[i] in st:
        break
    if st[i] != st2[i]:
        cost_diff+=1 
print(cost_diff)
