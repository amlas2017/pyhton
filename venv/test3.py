#5import numpy as np

n = input("Saisir un nombre  :")
n = int(n)

if (n > 0):
    if (n % 2 == 0):
        print("Nombre postif et pair.......\n")
    else:
        print("Nombre positif et impair......\n")

else:
    if (n % 2 == 0):
                    print("Nombre négatif et pair..........\n")
    else:
         print("Nombre négatif et impair.......")

