tab = [1,7,4,6,41,98,0,13,9,8]

def ordreCroissant(tab):
    for i in range(0,len(tab)):
        for j in range(0, len(tab)):
            if (tab[i] < tab[j]):
                aux = tab[j]
                tab[j] = tab[i]
                tab[i] = aux
    print(tab)

def ordreDecroissant(tab):
    for i in range(0,len(tab)):
        for j in range(0, len(tab)):
            if (tab[i] > tab[j]):
                aux = tab[j]
                tab[j] = tab[i]
                tab[i] = aux
    print(tab)


print("ordre croissant.............. 1")
print("ordre décroissant.............2")
print("Saisir votre choix   :")

n = int(input())
while (n not in [1,2]):
    print("ordre croissant.............. 1")
    print("ordre décroissant.............2")
    print("Saisir votre choix   :")
    print("Mauvais choix  !!!!!!!!")

if (n == 1) :
    ordreCroissant(tab)
    n = 1
else:
    ordreDecroissant(tab)
    n = 2
