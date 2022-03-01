import sys
import math
def max(x1,x2):
    if x1>x2:
        return x1
    return x2
list = []

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    list.append(t)

#print(list)
temperature= math.inf
for x in list:
    if abs(x)<=abs(temperature):
        if abs(x)<abs(temperature):
            temperature =x
        if abs(x)==abs(temperature):
            temperature =max(x,temperature)



if list:
    print(temperature)
else:
     print("0")
