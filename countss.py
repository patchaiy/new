pgi = int(input())
af,val = 3,3
while pgi > 0:
    if af == 0:
        val*=2
        af = val
    if pgi==1:
        print(af)
        break
    pgi -= 1
    af -= 1
