st1=input()
l=[]
for i in st1:
  if i not in l:
    l.append(i)
  else:
    break  
print(len(l))
