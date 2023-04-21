"""Napisz program do rozwiazywania rownania kwadratowego"""
import math
import cmath

def delta(a, b, c):
    res = pow(b, 2) - 4*a*c
    return res


while True:
    print("Program do wyznaczenia wyników równania kwad. Podaj współczynniki:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))


    if delta(a, b, c) < 0:
        print("Równanie kwadratowe nie ma rozwiązania.")
    elif delta(a, b, c) == 0:
        print("delta = 0, istnieje jedno rozwiązanie:")
        print("x1 = ", float(-1*(b/(2*a))))
    else:
        print("Równanie ma dwa rozwiązania.")
        print(cmath.sqrt(3))
        print(math.sqrt(3))
        x1 = ((-1*b) + math.sqrt(delta(a, b, c)))/(2*a)
        x2 = ((-1*b) - math.sqrt(delta(a, b, c)))/(2*a)
        print("x1 = ", x1)
        print("x2 = ", x2)