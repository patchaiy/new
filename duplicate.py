from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
str1=input()     
print(remove_duplicate(str1))
