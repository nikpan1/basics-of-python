from functools import cache
#from functools import lru_cache
import notmain


#@lru_cache(maxsize=5)
@cache
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


def main():
    for i in range(400):
        print(i, fib(i))


if __name__ == '__main__':
    main()


print(__name__)
print(notmain.__name__)