#prva zadaca
class Agol:
    def __init__(self, stepeni, minuti, sekundi):
        self.stepeni = stepeni
        self.minuti = minuti
        self.sekundi = sekundi

    def __str__(self):
        return f"agolot koj go vnesovte ima: {self.stepeni}* {self.minuti}' {self.sekundi}''"

    def my_print(self):
        return f"moja funkcija -> agolot koj go vnesovte ima: {self.stepeni}*{self.minuti}'{self.sekundi}''"

    def to_seconds(self):
        return f"agolot ima: {self.stepeni * 60 * 60 + self.minuti * 60 + self.sekundi} sekundi"
        #return self.stepeni * 60 * 60 + self.minuti * 60 + self.sekundi

    def is_valid(self):
        if self.stepeni < 0 or self.minuti < 0 or self.sekundi < 0:
            return False
        elif self.stepeni > 360 or self.minuti > 60 or self.sekundi > 60:
            return False
        else:
            return True

    def zbir_agli(self, vtor_agol):
        novi_stepeni = self.stepeni + vtor_agol.stepeni
        novi_minuti = self.minuti + vtor_agol.minuti
        novi_sekundi = self.sekundi + vtor_agol.sekundi
        #return Agol(novi_stepeni, novi_minuti, novi_sekundi) //vo ovoj slucaj ja koristi __str__ za pecatenje  
        return f"Noviot agol ima: {novi_stepeni}* {novi_minuti}' {novi_sekundi}''"

    def __add__(self, vtor_agol):
        novi_stepeni = self.stepeni + vtor_agol.stepeni
        novi_minuti = self.minuti + vtor_agol.minuti
        novi_sekundi = self.sekundi + vtor_agol.sekundi
        return Agol(novi_stepeni, novi_minuti, novi_sekundi)
    
my_agol1 = Agol(70,20,25)
print(my_agol1)
my_agol1.my_print()
print(my_agol1)
print(my_agol1.to_seconds())
print(my_agol1.is_valid())

my_agol2 = Agol(50,30,20)

zbir_na_agli = my_agol1.zbir_agli(my_agol2)
print(zbir_na_agli)

zbir_na_agli = my_agol1 + my_agol2
print(zbir_na_agli)

"""
# Python Program to find Perimeter of a Rectangle using length and width
def perimeter_of_Rectangle(length, width):
    return 2 * (length + width)

length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

perimeter = perimeter_of_Rectangle(length, width)
print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)
"""
"""
#vtora zadaca
class Krug:
    def __init__(self, radius):
        self.radius = radius

    def presmetka_na_plostina(self):
        PI = 3.14   
        return area =PI * self.radius * self.radius

    def presmetka_na_perimetar(self):
        PI = 3.14
        return circumference = 2 * PI * self.radius

my_krug = Krug(25)
print(my_krug.presmetka_na_perimetar)
"""
"""
radius = float(input("Enter the radius of the circle : "))
print("Circumference of the circle is : %.2f" % circumference)

r = float(input('Enter the radius of the circle :'))
        print("Area of the circle is : %.2f" %area)
"""