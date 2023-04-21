"""Napisz program, który prosi o podanie liczby naturalnej, a następnie wypisuje z ilu cyfr składa się wpisa-
na wartość, a także informację o sumie tworzących ją cyfr."""

a = int(input("a = "))
st = str(a)
res = int(0)

for i in range(0, len(st)):
    res += int(st[i])
print(res)


