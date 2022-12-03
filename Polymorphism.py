# Python does not support compile time polymorphism
# If there are multiple methods with the same name in a class or Python script,
# the method specified in the latter one will override the earlier one.


class Tiger:
    def food(self):
        print("Non-vegetarian")

    def color(self):
        print("Orange-Black")


class Elephant:
    def food(self):
        print("Vegetarian")

    def color(self):
        print("Gray")


t1 = Tiger()
e1 = Elephant()

t1.food()
t1.color()
e1.food()
e1.color()
