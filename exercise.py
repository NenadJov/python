godini = input("kolku godini imas?")
#print(type(godini))
try:
    godini = int(godini)
    if godini < 18:
        print("ne mozam da ti kazam")
    else:
        godina_na_raganje = 2020 - godini
        for x in range(godini):
            print(str(x+1) + "ej ti si roden " + str(godina_na_raganje) + " godina")
except:
    print("vnesi broj!")

new_list = ["nikola", "nenad", "zarko", "biljana"]
for item in new_list:
    print(item)