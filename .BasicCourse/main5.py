#Program w dwóch kolumnach wypisuje liczby pierwsze w odwrotnej kolejności
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

def perw(x):
    for i in range(2, int(x/2 + 1)):
        if x % i == 0:
            return 0    #false = 0
    return 1    #true = 1


def pr1(x):
    for i in range(x + 1, 100):
        if perw(i) == 1:
            return i
    return 0


def pr2(x):
    for i in range(1, x):
        if perw(x - i) == 1:
            return x - i
    return 0

print("Kolejne liczby pierwsze w dwóch kolumnach")
t1 = 1
t2 = 100
while True:
    t1 = pr1(t1)
    t2 = pr2(t2)
    if t1 == 0 or t2 == 1:
        break
    print(t1, " ", t2)