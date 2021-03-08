#  Write a function that prints the first letters of words from a specified string.

def first_letters(text):
    word_list = text.split(' ')
    word_list = [word[0] for word in word_list if word != '']
    letters = ' '.join(word_list)
    print(letters)


first_letters('  Welcome to  Prague    and have  a nice day!  ')
