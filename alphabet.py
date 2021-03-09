#  Write a function that prints the first (n) letters of the English alphabet.
#  If (n) is greater than 26, the letters are listed repeatedly.

def alphabet(n):
    alph_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    counter = 0
    while counter < n:
        for letter in alph_list:
            if counter < n:
                print(letter, end=' ')
                counter += 1
            else:
                break


alphabet(45)
