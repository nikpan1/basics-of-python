#  inheritance - dziedziczenie
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I say.")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # reference the super class - Pet class in this case
                                     # w skrócie odpala to co jest w __init__ w klasie Pet
        self.color = color

    def speak(self):
        print("meow")


class Dog(Pet):
    def speak(self):
        print("bark")


class Fish(Pet):
    pass


p = Pet("Tim", 18)
p.show()
d = Dog("Jill", 25)
d.speak()
f = Fish("Bubbles", 120)
f.speak()

c = Cat("Bill", 34, "Brown")
c.show()
c.speak()

