class Employee():

    procent_na_zgolemuvanje = 1.05

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = f"{name}.{surname}@gmail.com"
        self.plata = 18000

    def zgolemi_plata(self):
        self.plata = self.plata * self.procent_na_zgolemuvanje

    def __str__(self):
        return f"employee: name={self.name}, surname={self.surname}, age={self.age}, email={self.email}, plata={self.plata}"

class Developer(Employee):

    procent_na_zgolemuvanje = 1.1

    def __init__(self, name, surname, age, programming_language):
        super().__init__(name, surname, age)
        self.programming_language = programming_language
    
    # def zgolemi_plata(self):
    #     self.plata = self.plata * self.procent_na_zgolemuvanje

    def change_programming_language(self, language):
        self.programming_language = language

    def __str__(self):
        employee_for_print = super().__str__()
        return f"{employee_for_print} === developer for {self.programming_language}"

class Manager(Employee):

    procent_na_zgolemuvanje = 1.15

    def __init__(self, name, surname, age, developers):
        super().__init__(name, surname, age)
        self.managed_developers = developers

    def print_developers(self):
        for x in self.managed_developers:
            print("developer: " + x.name + " --> " + x.programming_language)

    def add_developer(self, developer):
        self.plata = self.plata * 1.03
        self.managed_developers.append(developer)

    def remove_developer(self, developer):
        self.managed_developers.remove(developer)
        if len(self.managed_developers) == 0:
            self.plata = self.plata/2
        else:
            self.plata = self.plata * 0.99

# employee1 = Employee("nikola", "stojkovski", 24)
# print(employee1)    
# employee1.zgolemi_plata()
# print(employee1)    
developer1 = Developer("nikola", "stojkovski", 24, "Python")
print(developer1)
developer2 = Developer("david", "stojanovski", 24, "Java")
print(developer2)
developer3 = Developer("marija", "filipovska", 25, "C++")
print(developer3)
# developer1.zgolemi_plata()
# developer1.change_programming_language('JavaScript')
# print(developer1)
list_developers = [developer1, developer2]
manager1 = Manager("zare", "prezime", 40, list_developers)
#manager1.add_developer(developer3)
manager1.remove_developer(developer1)
manager1.print_developers()
print(manager1)