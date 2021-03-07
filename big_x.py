# Write a function that draws a capital letter X of size (n) from the characters '#'.
def big_x(n):
    for i in range(n):
        for j in range(n):
            if i + j == n - 1 or i - j == 0:
                print('#', end='')
            else:
                print(' ', end='')
        print()


big_x(7)
