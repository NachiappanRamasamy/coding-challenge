ip = int(input())

from math import factorial

for i in range(ip):
    for j in range(ip-i-1):
        print(end=" ")
 
    for k in range(i+1):
        print(factorial(i)//(factorial(i-k)*factorial(k)), end=" ")
    print()
