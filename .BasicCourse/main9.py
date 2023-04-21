#silnia na dwa sposoby
import math
import timeit

def factorialone(x):
    res = 1
    for i in range(1, x + 1):
        res *=i
    return res


def factorialtwo(x, a):
    if x != 1:
        return factorialtwo(x - 1, a * x)
    return a

val = int( input("Podaj liczbe:") )
print(val, "! :", )

start = timeit.default_timer()
print("I. ")
print(factorialone(val))
end = timeit.default_timer()
print("Czas trwania - {}s.".format(end-start))

start = timeit.default_timer()
print("II. ")
print(factorialtwo(val, 1))
end = timeit.default_timer()
print("Czas trwania - {}s.".format(end-start))

start = timeit.default_timer()
print("III. ")
print(math.factorial(val))
end = timeit.default_timer()
print("Czas trwania - {}s.".format(end-start))
