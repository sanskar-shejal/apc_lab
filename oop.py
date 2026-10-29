class DestructorDemo:
    def __init__(self, name):
        self.name = name
        print(f"  [Init] Object '{self.name}' initialized.")

    def __del__(self):
        print(f"  [Destructor] Object '{self.name}' is destroyed.")


class AccessSpecifierBase:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self._roll_no = roll_no
        self.__marks = marks

    def display(self):
        print(f"Public name: {self.name}")
        print(f"Protected _roll_no: {self._roll_no}")
        print(f"Private __marks: {self.__marks}")

    def get_private_marks(self):
        return self.__marks


class AccessSpecifierDerived(AccessSpecifierBase):
    def test_access(self):
        print("Derived accessing public:", self.name)
        print("Derived accessing protected:", self._roll_no)
        print("Derived accessing private via mangled name:", self._AccessSpecifierBase__marks)


class Car:
    def move(self):
        return "Car is driving smoothly on the road."


class Boat:
    def move(self):
        return "Boat is sailing gracefully through the water."


def start_moving(vehicle):
    print(vehicle.move())


class OverloadedNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return OverloadedNumber(self.value + other.value)

    def __str__(self):
        return f"OverloadedNumber({self.value})"


def main():
    print("Object Destructor (__del__):")
    obj = DestructorDemo("Alpha")
    del obj

    print("\nAccess Specifiers (Public, Protected, Private):")
    acc_obj = AccessSpecifierDerived("Viraj", 24, 95)
    acc_obj.test_access()

    print("\nDuck Typing:")
    start_moving(Car())
    start_moving(Boat())

    print("\nOperator Overloading (+ and str):")
    n1 = OverloadedNumber(25)
    n2 = OverloadedNumber(75)
    n3 = n1 + n2
    print(f"{n1} + {n2} = {n3} (Result value: {n3.value})")


if __name__ == "__main__":
    main()
