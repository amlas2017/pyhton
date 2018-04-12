import  numpy as np

n = int(input("donner un nombre :"))

def fact(i):
    if (i == 0) or (i == 1):
        return 1
    else: return i*fact(i-1)

print(fact(n))