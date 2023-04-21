

def check(tab):
    for q in range(1, 3):
        for p in range(0, 3):
            if tab[0][p] == tab[1][p] and tab[2][p] == tab[1][p] and tab[0][p] == q:
                return q  # wygrał gracz 1
            if tab[p][0] == tab[p][1] and tab[p][2] == tab[p][1] and tab[p][0] == q:
                return q  # wygrał gracz 1
        if tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[0][0] == q:
            return q
        if tab[2][0] == tab[1][1] and tab[1][1] == tab[0][2] and tab[2][0] == q:
            return q
    return 0

def main():
    print("tictactoe")
    tab = [[0 for m in range(3)] for n in range(3)]
    tab[2][0] = 2
    tab[1][1] = 1
    tab[0][2] = 2
    # 1 = x
    # 2 = o
    print(check(tab))


if __name__ == '__main__':
    main()
