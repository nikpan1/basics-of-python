"""Napisz program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika. Wartość stałej
π weź z biblioteki math. Promień nie może być ujemny. W przypadku podania liczby ujemnej, program
powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć."""
import cmath
import math

def pole(r):
    result = cmath.pi*2*r
    return result

def obj(r):
    result = cmath.pi*math.pow(r, 2)
    return result

while True:
    promien = float(input("Podaj promień r = "))
    if promien < 0 or promien == 0:
        print("Promień musi być dodatni.")
        continue
    print("Pole = ", pole(promien))
    print("Obj = ", obj(promien))

