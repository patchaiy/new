nui=input()
m= 0
for i in range(0,len(nui)-1):
  for j in range(i+1,len(nui)):
    l=nui[i:j+1]
    if l==l[::-1]:
      if len(l) > m:
        m = len(l)
        k=l
print(k)
