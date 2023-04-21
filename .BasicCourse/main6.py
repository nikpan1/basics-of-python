#liczby doskonałe

def dosk(a):
    count = 0
    for i in range(1, a):
        if a % i == 0:
            count += i

    if count == a:
        return 1 #true = 1
    return 0 #false = 0


t = 100

for i in range(1, t):
    if dosk(i) == 1:
        print(i)
