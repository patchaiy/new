number1234 = int(input())
resty = []
for i in range(pow(2, number1234)):
    resty.append(bin(i)[2:].zfill(number1234))
resty.sort(key=(lambda x: x.count('1')))
for i in resty:
    print(i) 
