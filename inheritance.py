# parent class
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Name : " ,self.name)
        print("Age : ", self.age)


# child class
class Employee(Person):
    def __init__(self, name, age, id, salary):
        # invoking __init__ of the parent class
        Person.__init__(self, name, age)
        self.id = id
        self.salary = salary

    def intro(self):
        print("Name : " ,self.name)
        print("Age : ", self.age)
        print("ID : ", self.id)
        print("Salary : ", self.salary)


p1 = Person("Suraj", 22)
e1 = Employee("Dhiraj", 25, 1001, 100000)
p1.intro()
e1.intro()   # This is also runtime polymorphism method overriding

