# task 1 
from abc import ABC, abstractmethod

class Ship(ABC):
    
    def __init__(self, name, year, size):
        self.name = name
        self.year = year
        self.size = size

    @abstractmethod
    def ship_type(self): pass

    def __str__(self):
        return f"\nName: {self.name}\nYear: {self.year}\nSize: {self.size}"

class Frigate(Ship): 
    def __init__(self, name, year, size, speed):
        super().__init__(name, year, size)
        self.speed = speed

    def ship_type(self):
        return "Type: Frigate"

    def __str__(self):
        return f"{super().__str__()}\nSpeed: {self.speed}km/sec"

class Destroyer(Ship):
    def __init__(self, name, year, size, sits):
        super().__init__(name, year, size)
        self.sits = sits

    def ship_type(self):
        return "Type: Destroyer"

    def __str__(self):
        return f"{super().__str__()}\nSits: {self.sits}"

class Cruiser(Ship):
    def __init__(self, name, year, size, model):
        super().__init__(name, year, size)
        self.model = model

    def ship_type(self):
        return "Type: Cruiser"

    def __str__(self):
        return f"{super().__str__()}\nModel: {self.model}"


f = Frigate("Frigate", 1996, 325, 210)
d = Destroyer("Destroyer", 1963, 320, 40)
c = Cruiser("Cruiser", 1963, 320, "super model")

print(f)
print(f.ship_type())

print(d)
print(d.ship_type())

print(c)
print(c.ship_type())

# task 2
class Airplane:
    def __init__(self, model, max_psngrs):
        self.model = model
        self.max_psngrs = max_psngrs
        self.psngrs = 0

    def __eq__(self, other):
        return self.model == other.model and self.max_psngrs == other.max_psngrs

    def __add__(self, number):
        if self.psngrs + number <= self.max_psngrs:
            self.psngrs += number
        else:
            print(">> there are already too many passengers")
        return self

    def __iadd__(self, number):
        return self.__add__(number)

    def __sub__(self, number):
        if self.psngrs - number < 0:
            self.psngrs = 0
        else:
            self.psngrs -= number
        return self

    def __isub__(self, number):
        return self.__sub__(number)

    def __gt__(self, other):
        return self.max_psngrs > other.max_psngrs

    def __ge__(self, other):
        return self.max_psngrs >= other.max_psngrs

    def __lt__(self, other):
        return self.max_psngrs < other.max_psngrs

    def __le__(self, other):
        return self.max_psngrs <= other.max_psngrs

    def __str__(self):
        return f"{self.model} has {self.psngrs}/{self.max_psngrs} passengers"

a_1 = Airplane('F-16', 10000)
a_2 = Airplane('Cy-29', 735)

print(a_1 == a_2)   

a_2 += 100
print(a_2) 

a_2 -= 500
print(a_2)

print(a_1 > a_2)  
