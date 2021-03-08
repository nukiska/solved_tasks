#  Write a function that returns the specified string and replaces X with every other character.

def censorship(text):
    text_list = list(text)
    for i in range(1, len(text_list), 2):
        text_list[i] = 'X'
    text = ''.join(text_list)
    return text


print(censorship('This is a secret message'))
