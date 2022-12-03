class Dog:
    # instances
    attr1 = "mammal"

    # Constructor
    def __init__(self, name):
        self.name = name;

    def speak(self):
        print("My name is ", self.name)


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# instance variable
print(Rodger.name)
print(Tommy.name)

# class variable
print(Dog.attr1)
print(Tommy.attr1)   # class variables can be accessed by class and object name

# class methods
Rodger.speak()
Tommy.speak()


