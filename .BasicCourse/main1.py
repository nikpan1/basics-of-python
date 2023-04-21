import random

print('tekst')
print('tekst' + 'tekst2')
a=1
print(a)
print(a, a+1)
#komentarz
""" 
długi
komentarz
"""
print(' ')
print(type(a))
print(type(a) is int)
print(dir(a)) #lol

print(' ')
from math import pi, cos
print(cos(pi))      #-1

print(' ')
#zmiana typu
a=-1
print('przed = ', a)
b=str(a)
print(b)
print(type(b))
c = (float(b))
print("po float = ", c)

print(' ')
#tablica
lista = [ 1, 2, 3]
tupla = tuple(lista)
print(tupla)

print(' ')
#funkcja
def funkcja(a):
        wynik = a**2
        return wynik
d=funkcja(3)
print(d)

#wyłapywanie błędów be like

try:
    print(2/0)
    print(int('tekst'))
except ZeroDivisionError:
    print('wychwycony błąd = ', ZeroDivisionError)
except ValueError:
    print('ERROR')
else:
    print(" non error")

#instukcja warunkowa if
a = random.randint(0, 10) #losowanie liczb z przedziału od 0 do 10
if a > 5:
    print('liczba wylosowana jest większa od 5')
elif a == 5:
    print('liczba jest równa 5')
else:
    print('Wylosowana liczba jest mniejsza od 5')


#pętla while
i=0
while i < 3:
    print(i)
    i += 1

#pętla for
for liczba in range(3):
    print(liczba)

for liczba in range (3, 5):
    print(liczba)


#tablica str
s = 'test'
print('test', s[0], s[2])

#formatowanie łańcucha znaków
imie = 'Nikodem'
nazwisko = 'Kowalski'

tekst = "Imię: " + imie + ", nazwisko: " + nazwisko
print("1.", tekst)
tekst = "Imię: %s, nazwisko: %s" % ( imie, nazwisko)
print("2.", tekst)
tekst = "Imię: {}, nazwisko: {}".format( imie, nazwisko)
print("3.", tekst)
tekst = "Imię: {one}, nazwisko: {two}".format(one=imie, two=nazwisko)
print("4.", tekst)

print(" ")
#rodzaje formatu wyświetlanych liczb
l = 10
tekst2 = "1. Liczba {} z użyciem :d - {:d}".format(l, l)
print(tekst2)
tekst2 = "2. Liczba {} z użyciem :f - {:f}".format(l, l)
print(tekst2)
tekst2 = "3. Liczba {} z użyciem :.2f - {:.2f}".format(l, l)
print(tekst2)
tekst2 = "Liczba {} z użyciem :+d - {:+d}".format(l, l)
print(tekst2)

print(" ")
#znaki specjalne
print("1 2 3")
print("\n1 2 3")
print("\t1 2 3")
print("\'1 2 3")
print("\"1 2 3")
print("\\1 2 3")    #dlaczego \ nie starczy to pokazane poniżej
print("\1 2 3")

tekst3 = "jeden,dwa,trzy"
print(tekst3)
tekst3.split(',')
print(tekst3)
lista = ['jeden', 'dwa', 'trzy']
print(';'.join(lista))

#tablice wywołwyanie, indeksowanie etc.
lista = [1, 2.5, 'trzy']
print(lista)
print(lista[1])
print(lista[-1])    # element -n to nty wyraz od końca
prawda = '1' in lista
print(prawda)
print(lista.index('trzy'))

#działania na tablicach

list1 = [1, 2, 3]
list2 = [4, 5]
print(list1, list2)
list2.append(6) #dodanie wyrazu '6' na koniec tabeli
print(list1, list2)
list1.extend(list2) # połączenie list1 i list2 w list1
print(list1, list2)
del list1[0]
print(list1, list2)

#definiowanie tupli - takich tablic, które służą tylko do odczytu
tupla = (1, 2, 3, 4, "piec")
print(tupla[0])
print(tupla[1:3])
print(tupla.index("piec"))

#słownik dict