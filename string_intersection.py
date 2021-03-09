#  Write a function that lists the letters that are in the same position in both strings for the two strings entered.

def string_intersection(left, right):
    shorter_string = left if len(left) <= len(right) else right
    for i in range(len(shorter_string)):
        if left[i] == right[i]:
            print(shorter_string[i])


string_intersection('WORLD', 'WORD')
