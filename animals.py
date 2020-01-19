class Animal:
    def __init__(self, color, age):
        self.boja = color
        self.godini = age

    def __str__(self):
        return "animal object has: " + self.boja + " - " + str(self.godini) + "!!!"

class Dog(Animal):
    def __init__(self, color, age, has_tail):
        super().__init__(color, age)
        self.has_tail = has_tail

my_dog = Dog('black', 3, True)

print(my_dog.boja)

#my_dog = Animal("dog","black", 3)
print(my_dog)
