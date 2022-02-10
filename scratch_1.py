from math import sqrt

prim = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
be = int(input("Add meg a számot: "))
tenyezok = []
bontas = {}

def szamolas(be):
    count = 0
    while be % 2 == 0:
        print(2)
        tenyezok.append(2)
        count += 1
        be = be / 2
        bontas[2] = count
    for i in prim:
        while be % i == 0:
            print(i)
            be = be / i
            tenyezok.append(i)
            for j in tenyezok:
                bontas[i] = tenyezok.count(j)
    if be > 2:
        print(be)


def ellenorzes():
    if prim[-1] > sqrt(be):
        print("Nem biztos, hogy megtudom határozni")
        szamolas(be)
    else:
        szamolas(be)
ellenorzes()

print(bontas)




'''
def szamolas(n):
    # even number divisible
    while n % 2 == 0:
        print(2),
        n = n / 2

    # n became odd
    for i in range(3, int(sqrt(n)) + 1, 2):

        while (n % i == 0):
            print(i)
            n = n / i

    if n > 2:
        print(n)

szamolas(n)
'''