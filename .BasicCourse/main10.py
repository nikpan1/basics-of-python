import math
import time
import random


def rv():
    a = time.time_ns()
    a = int((a / 100) % pow(10, 8))
    b = int(math.sqrt(a + time.time_ns()))
    rand = int((pow(b, 4) - math.sqrt(a)) % (a / 6))
    return rand


def section(p, q):
    a = rv()
    if a < p:
        while a > p:
            a *= 1.2
    elif a > q:
        while a > q:
            a = a / 6.7
    return int(a)


x = 1
y = 1000
guess = section(x - 1, y - 1)       #guess - liczba zgadywana
val = int((x+y)/2)      #val - liczba zgadującego
print("A: Program do zgadywania liczby.")
print("A: Podaj liczbę z przedziału [{0}, {1}]:".format(x, y))


while True:
    print("B: Podaje {0}.".format(val))

    if val == guess:
        print("A: Brawo zgadłeś!")
        print("B: Ha!")
        break
    elif val > guess:
        print("A: Podałeś za dużą liczbę.")
        y = val
        val = int((x+val)/2)
    else:
        print("A: Podałeś za małą liczbę.")
        x = val
        val = int((val+y)/2)

    print("A: Podaj liczbę jeszcze raz: ")
