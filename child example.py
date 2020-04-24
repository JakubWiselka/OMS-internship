class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        

class Employee(Person):
    def __init__(self, name, surname, age, position, specialisation):
        super().__init__(name, surname, age)
        self.position = position
        self.specialisation = specialisation


class Client(Person):
    def __init__(self, name, surname, age, order, date):
        super().__init__(name, surname, age) #Pobiera __init__ z rodzica tak samo można z karzdą funkcją
        self.order = order
        self.date = date

    def zamowienie(self):
        print(self.order)




# pracownik = Employee("Tomek", "Kowalski", 23, "Programer", "Python")
# print(pracownik.name)
# print(pracownik.position)

klient = Client("Jakub","Wisełka",50,"website","Java")
klient.zamowienie()


