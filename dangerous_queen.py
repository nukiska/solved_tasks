#  Write a function that shows the squares of the chessboard threatened by a queen at position (x, y).
#  The output consists of a table marked with dots, the position of the queen is marked with the letter Q.
#  The fields that the queen threatens are marked with an asterisk. The queen threatens the squares horizontally,
#  vertically and diagonally. You can assume that the inputs are numbers from 1 to 8.

def queen(x, y):
    for row in range(8):
        for col in range(8):
            if row == y - 1 and col == x - 1:
                print('Q', end=' ')
            elif row == y - 1 or col == x - 1 or row + col == x + y - 2 or col - row == x - y:
                print('*', end=' ')
            else:
                print('.', end=' ')
        print()


queen(5, 4)
