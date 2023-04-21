"""Zadanie 3
Napisz program proszący użytkownika o podanie dwóch liczb a i b i wypisujący ich sumę, różnicę, iloczyn,
iloraz, √a + b oraz a^b."""

import math


def suma(a, b):
    return a+b


def inf(a, b):
    return math.sqrt(a+b)


def power(a, b):
    return math.pow(a, b)

while True:
    print("Podaj wartości by wyznaczyć pierwiastki")
    a = float(input("a = "))
    b = float(input("b = "))
    print("a+b = ", suma(a, b))
    print("pierwiastek z a+b = ", inf(a, b))
    print("Potega a do b = ", power(a,b))
