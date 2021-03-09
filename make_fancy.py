#  Write a function that prints the given string diagonally and (n) times in a row.

def make_fancy(text, n):
    counter = 0
    for i in range(len(text)):
        print(' ' * counter, end='')
        for j in range(n):
            print(text[i], end=' ')
        counter += 1
        print()


make_fancy('WELCOME', 3)
