#prva zadaca
class Agol:
    def __init__(self, stepeni, minuti, sekundi):
        self.stepeni = stepeni
        self.minuti = minuti
        self.sekundi = sekundi

    def __str__(self):
        return f"agolot koj go vnesovte ima: {self.stepeni}* {self.minuti}' {self.sekundi}''"
    
my_agol1 = Agol(70,20,25)
print(my_agol1)


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