#  Write a function that draws a text board with a side of given size (n).
#  The checkerboard squares should be formed by the characters '.' and '#'.

def chessboard(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()


chessboard(6)
