# from helper import zbir_na_elementi_na_niza_deleno_so_dva, my_print
from helper import *

my_print()

n = int(input("vnesi broj na elementi: "))
a = int(input("vnesi go prviot element: "))
b = int(input("vnesi go prviot element: "))

niza = [a, b]
for x in range(n-2):
    new_element = zbir_na_elementi_na_niza_deleno_so_dva(niza)
    niza.append(new_element)

print(niza)

