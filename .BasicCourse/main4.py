import random
val = random.randint(0,10)
while True:
    a = int(input("Zgaduj liczbe: "))
    if a > val:
        print("Podana liczba jest za duża")
    elif a < val:
        print("Podana liczba jest za mała")
    elif a == val:
        print("Brawo, zgadłeś liczbę.")
        break


print("Program do liczby Catalana")
a = float(1)
for i in range(1, 10):
    print(a)
    a *= (4*i+2)/(i+2)