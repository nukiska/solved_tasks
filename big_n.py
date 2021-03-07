#  Write a function that prints a text image of a capital letter N on (n) lines.

def big_n(n):
    for i in range(n):
        for j in range(n):
            if i == 0 and j == n - 1:
                print('|\\' + (n - 1) * ' ' + '|')
            if 0 < i < (n - 1) and j == n - 1:
                print('|' + i * ' ' + '\\' + (n - i - 1) * ' ' + '|')
            if i == n - 1 and j == n - 1 and n != 1:
                print('|' + (n - 1) * ' ' + '\\|')


big_n(4)
