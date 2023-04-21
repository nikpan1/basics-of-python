# intermidiate


# set
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

print(myset.pop())
print(myset)

for x in myset:
    print(x)

if 4 in myset:
    print("!!!4")
if 2 in myset:
    print("!!!2")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}

u = odds.union(evens)
print(u)


# lambda
print("\n\nLambda")
add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x*y
print(mult(3, 5))




