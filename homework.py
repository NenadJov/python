"""
#cetvrta zadaca
# from helper import zbir_na_elementi_na_niza_deleno_so_dva, my_print
from helper import *

#my_print()

n = int(input("vnesi broj na elementi: "))
a = int(input("vnesi go prviot element: "))
b = int(input("vnesi go prviot element: "))

niza = [a, b]
for x in range(n-2):
    new_element = zbir_na_elementi_na_niza_deleno_so_dva(niza)
    niza.append(new_element)

print(niza)

#prva zadaca
sekundi = int(input('Vnesi cel broj na sekundi!'))
x = sekundi 
y = x / 3600
print('vneseniot broj na sekundi e transformiran vo:')
print('casovi:')
print(int(y))
z = x - int(y)*3600 
m = z / 60
print('minuti:')
print(int(m))
q = int(y) * 3600
w = int(m) * 60
d = x - q - w
print('sekundi:')
print(d)

#vtora zadaca
palindrom = int(input('Vnesi trocifren broj za da proveram dali e palindrom:'))
if len(str(palindrom)) != 3:
    print('Nevaliden vnes, vneseniot broj treba da sodrzi tri cifri')
else:
    niza = [int(x) for x in str(palindrom)]
    if niza[0] == niza[2]:
        print('Brojot e palindrom')
    else:
        print('Brojot ne e palindrom')
"""
#treta zadaca
prva_strana_na_triagolnik = int(input('Vnesi dimenzija na prvata strana na triagolnikot: '))
vtora_strana_na_triagolnik = int(input('Vnesi dimenzija na vtorata strana na triagolnikot: '))
treta_strana_na_triagolnik = int(input('Vnesi dimenzija na tretata strana na triagolnikot: '))
strana_na_kvadrat = int(input('Vnesi dimenzija na strana na kvadratot: '))
x = prva_strana_na_triagolnik + vtora_strana_na_triagolnik + treta_strana_na_triagolnik
y = 4 * strana_na_kvadrat
if x > y:
    print('Triagolnik')
elif x < y:
    print('Kvadrat')
else:
    print('Isti se')