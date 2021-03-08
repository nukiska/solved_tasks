#  Write a function that prints the given text "zigzag" on two lines with spaces marked with dots.

def zigzag(text):
    global dot_text  # global variable 'dot_text' is undefined at the module level
    for i in range(1, -1, -1):
        text_list = list(text)
        for j in range(i, len(text), 2):
            text_list[j] = '.'
            dot_text = ''.join(text_list)
        print(dot_text)


zigzag('WELCOME')
