import random


def min(arr):
    minimum = 100
    index = 0
    for h in range(len(arr)):
        if minimum > arr[h]:
            minimum = arr[h]
            index = h
    return index


# sortowanie przez wybor
def sort(arr):
    a = 0
    for p in range(0, len(arr)):
        index = p + min(arr[p:len(arr)])
        a = arr[index]
        arr[index] = arr[p]
        arr[p] = a
    return arr


def main():
    print("elo")
    arr = []
    for g in range(0, 100):
        arr.append(random.randint(0, 100))

    print(arr)
    arr = sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
