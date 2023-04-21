x_size, y_size = 10, 10
arr = [[-1 for mx_fi in range(x_size + 1)] for ny_ni in range(y_size + 1)]

size = x_size
half = size / 2
print(half)
k = 0
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j == half:
            for t in range(j, k + 1 + j):
                arr[i][t] = 10
            half -= 1
            k += 2

for i in arr:
    print(i)

