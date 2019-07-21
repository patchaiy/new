PS = int(input())
QS = []
Di = PS//2 + PS
for X in range(1,PS+1):
  if X%2==0:
    QS.append(X)
for X in range(1,PS+1):
  if X%2!=0:
    QS.append(X)
for X in range(1,PS+1):
  if X%2==0:
    QS.append(X)
print(Di)
print(*QS)
