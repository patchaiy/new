import sys 
def inCoinsi(coinsi, mo, V): 
    if (V == 0): 
        return 0
    res = sys.maxsize 
    for i in range(0, mo): 
        if (coinsi[i] <= V): 
            sub_res = inCoinsi(coinsi, mo, V-coinsi[i]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1 
    return res
n,V=list(map(int,input().split()))
coinsi = list(map(int,input().split())) 
mo= len(coinsi) 
print(inCoinsi(coinsi, mo, V)) 
