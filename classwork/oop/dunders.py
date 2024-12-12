from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self):
        pass

    def __str__(self) -> str:
        return self.name


# inheritamce: class Deriver(Base)
class Rectangle(Figure):
    def __init__(self, width, height) -> None:
        # super() - reference to base class
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"{self.name}: {self.width}x{self.height}cm"

    def __int__(self) -> int:
        return self.area()

    # ---- operator overloading ----
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()

    def area(self):
        return self.width * self.height


f1 = Rectangle(123, 88)
f2 = Rectangle(20, 30)

f3 = f1 + f2
print(f3)
print(f"Area: {f3.area()}cm^2")
print(f"Area: {int(f3)}cm^2")

print("Rect 1 > Rect 2:", f1 > f2)
print("Rect 1 < Rect 2:", f2 < f1)

print("Rect 1 == Rect 2:", f2 != f2)
print("Rect 1 == Rect 2:", f2 == f2)