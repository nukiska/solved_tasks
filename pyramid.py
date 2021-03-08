#  Write a function that draws a text image of a pyramid of height (n).

def pyramid(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end=' ')
        print('# ' * counter, end=' ')
        counter += 2
        print()


pyramid(5)
