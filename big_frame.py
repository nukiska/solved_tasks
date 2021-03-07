# Write a function that for given list of words will write these words on one line
# and make a frame of the '+' character around them.

def big_frame(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    print('+' * (max_length + 2))
    for word in word_list:
        free_space = max_length - len(word)
        print('+' + word + free_space * ' ' + '+')
    print('+' * (max_length + 2))


big_frame(['Welcome', 'to', 'Prague'])
