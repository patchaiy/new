B,S=map(str,input().split("|"))
Ci=input()
if  len(B)>len(S):
    if len(B)==len(S)+len(Ci):
        print(B+"|"+S+Ci)
elif len(B)<len(S):
     if len(S)==len(B)+len(Ci):
        print(B+Ci+"|"+S)
elif len(B)==len(S) and len(Ci)>1 or (len(S) or len(B)):
    print("impossible")
