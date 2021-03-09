#  Write a function that draws a text square of size (n) that has a dots in the middle and a grid edge.

def empty_square(n):
    for i in range(n):
        print('#', end=' ')
        for j in range(n - 2):
            if i == 0 or i == n - 1:
                print('#', end=' ')
            if 0 < i < n - 1:
                print('.', end=' ')
        if n != 1:
            print('#', end=' ')
        print()


empty_square(7)
