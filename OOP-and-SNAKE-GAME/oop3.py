class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


Person.number_of_people = 4
p1 = Person("tim")
p2 = Person("jill")
print(p2.number_of_people)
print(p1.number_of_people)
print(Person.number_of_people_())


