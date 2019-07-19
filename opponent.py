ki=int(input())
s=0
for p in range(0,ki):
  if(pow(2,p)>ki):
    break
  s=ki-pow(2,p)
print(s)

