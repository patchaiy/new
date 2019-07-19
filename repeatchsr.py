st=input()
l=[]
for i in st:
  if i not in l:
    l.append(i)
  else:
    break  
print(len(l))
