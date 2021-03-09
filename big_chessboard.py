def big_chessboard(n, m):
    for k in range(n):
        for j in range(m):
            for i in range(n):
                if i % 2 == 0 and k % 2 == 0:
                    print('#' * m, end='')
                elif i % 2 != 0 and k % 2 != 0:
                    print('#' * m, end='')
                else:
                    print('.' * m, end='')
            print()


big_chessboard(5, 3)
