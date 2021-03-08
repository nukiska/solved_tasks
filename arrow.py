#  Write a function that draws a text image of an arrow from the characters '*'
#  inside a square of size (n) formed by dots. You can assume that (n) is odd.

def arrow(n):
    for i in range(n):
        for j in range(n):
            counter = '.'
            if i == n // 2 or j - i == n // 2 or i + j == n // 2 + (n - 1):
                counter = '*'
            print(counter, end='')
        print()


arrow(7)  # odd number
