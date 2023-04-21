x = 11
if x in [1, 2, 3]:
    print("x jest w przedziale")

def repeatball():
    try:
        print(a)
        print("Funkcja zadziałała")
    except:
        print("Funkcja NIE zadziałała")
        return True

if repeatball():
   not_catched = False




zdanie = "Hello World"
st = zdanie.split(" ")
print(st)
print(st[1])
print(0.5 *10)
"""import random
import time
# możliwe, że do zmiany
def search_in_text(word, long):
    for i in range(0, len(long)):
        if long[i] == word[0]:
            if word == long[i:(i+len(word))]:
                print(long[i:(i+len(word))])
                return True
    return False
# print(f'word[{j}] = long[{j + i}], {word[j]} = {long[j+i]}')
l = "testuje moja funkcje"
x = "Funkcja"
print(search_in_text(x, l))
print(len(x))
t = random.randrange(100, 250, 1)
t = t / 100
time.sleep(t)"""