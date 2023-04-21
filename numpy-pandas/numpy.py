import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.expand_dims(a, axis=1)

print(a)
print(a.shape)
print(" ")
print(b)
print(b.shape)
c = np.expand_dims(b, axis=0)
print(c)
print(c.shape)

#____________________
data = np.array([1, 2, 3])
print("\n\n")
print(data)
print("data[0] = ", data[0])
print("data[1] = ", data[-1])
print(data[2:3])
print(data[:2])
print(data[0:3])

print(" ")
five_up = (data >= 5)
print(data[five_up])
print(data[data > 2])

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
h = np.arange(100)
div2 = a[a % 2 == 0]
print("a = ", a, "\ndiv2 = ", div2)
print("h = ", h, "\ndiv2 = ", h[h % 2 == 0])


q = np.zeros((2, 3))
print(q)

p = np.zeros((4, 6), dtype='int32')
print(p)

y = np.full((2, 8), 50, dtype='float32')
print(y)


m = np.full_like(y, 1)
print(m)

e = np.random.rand(4, 2)
print(e)

g = np.random.randint(-7, 7, size=(3, 6))
print(g)

r = np.identity(5)
print(r)

arr = np.array([1, 2, 3])
r1 = np.repeat(arr, 5)
print(r1)
arr = np.array([[1, 2, 3]])
r2 = np.repeat(arr, 3, axis=0)
print(r2)
r3 = np.repeat(arr, 3, axis=1)
print(r3)

# Zadanie
output = np.ones((5, 5))
print(output)
z = np.zeros((3, 3))
z[1, 1] = 9
print(z)
output[1:4, 1:4] = z
print(output)


# uwaga w kopiowaniu

lista = np.array([1, 2, 3])
print(lista)
link = lista
link[0] = 100
print(lista)

# trzeba tak:

lista = np.array([1, 2, 3])
print(lista)
kopia = lista.copy()
kopia[0] = 100
print(kopia)


# działania arytm.
a = np.array([1, 2, 3, 4])
print("a = ", a)
print("a + 2 = {0},\na * a = {1},\na / 2 = {2}".format(a+2, a*a, a/2))

b = np.array([5, 4, 3, 2])
print("a = {0},\nb = {1},\na + b = {2}".format(a, b, a + b))

print(np.cos(a))

# algebra liniowa
a = np.ones((2, 3))
b = np.full((3, 2), 2)
print(a, "\n", b)
print(np.matmul(a, b))
c = np.identity(3)
print(np.linalg.det(c))


#statystyki

stats = np.array([[1, 2, 3], [1, 4, 5]])
print(np.min(stats))
print(np.min(stats, axis=0))

print(np.sum(stats))
print(np.sum(stats, axis=1))


# zmiana kształtu
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape((1, 8))
print(after)
after = before.reshape((4, 2))
print(after)

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.hstack((v1, v2, v1, v2)))


# Zaawansowane indeksowanie i boolowanie

a = np.ones((10, 5))
print(a)
print(a > 10)
print(data)
print(data[data > 2])
print(data[[1, 2]])
print(np.any(a > 50, axis=0))

