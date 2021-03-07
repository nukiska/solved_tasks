# Write a function that calculates the highest sum of two consecutive numbers for a given list of positive numbers.

def max_pair_sum(num_list):
    i = len(num_list)
    max_sum = 0
    while i != 1:
        pair_sum = num_list[i - 1] + num_list[i - 2]
        if pair_sum > max_sum:
            max_sum = pair_sum
        i -= 1
    return max_sum


print(max_pair_sum([7, 3, 6, 9, 5, 1, 2, 8, 3, 4, 1]))
