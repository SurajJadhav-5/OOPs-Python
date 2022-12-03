#  Encapsulation describes the idea of wrapping data and the methods that work on
#  data within one unit.
class Base:
    def __init__(self):
        # Public member
        self.c = 100
        # protected member
        self._a = 10
        # private member  --> Encapsulation
        self.__b = 20

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Public mamber : ", self.c)
        print("Protected mamber : ", self._a)
        # print("Private mamber : ", self.__b) # This is Encapsulation
        # we can not access private members directly


b = Base()
d = Derived()
