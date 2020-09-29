# Given a list of integers n_1, n_2 to n_i, produce a list of all possible fractions group by value
# Input: A list of integers, 1 <= n_i <= 24
# Output: A list of fractions grouped by value in the form 'numerator-denominator'

# Test 1: [1, 3, 5] => [[1-5], [1-3], [2-5], [3-5], [2-3], [4-5], [1-1, 3-3, 5-5]]
# Test 2: [1, 3, 5, 12] => [[1-12], [2-12], [1-5], [3-12], [1-3, 4-12], [2-5], [5-12], [6-12], [7-12], [3-5], [2-3, 8-12], [9-12], [4-5], [10-12], [11-12], [1-1, 3-3, 5-5, 12-12]]

# Naive
def find_fraction(fraction_string):
    numbers = [int(i) for i in fraction_string.split('-')]
    # print(numbers[0] / numbers[1])
    return numbers[0] / numbers[1]

def naive_grouped_fractions(number_list, print_result=False):
    unsorted_fractions = []

    # Create list full of every value
    for number in number_list:
        unsorted_fractions += [f'{i}-{number}' for i in range(1, number+1)]

    # Sort array
    sorted_fractions = sorted(unsorted_fractions, key=lambda string: find_fraction(string))

    # Group
    result = []
    holding_list = []
    for i in range(0, len(sorted_fractions)):
        if i == 0 or find_fraction(sorted_fractions[i]) == find_fraction(sorted_fractions[i-1]):
            holding_list.append(sorted_fractions[i])
        elif find_fraction(sorted_fractions[i]) != find_fraction(sorted_fractions[i-1]):
            result.append(holding_list)
            holding_list = [sorted_fractions[i]]

        if i+1 == len(sorted_fractions):
            result.append(holding_list)

    if print_result:
        print(result)


# Test 1: [1, 3, 5]
naive_grouped_fractions([1, 3, 5], True)

# Test 1: [1, 3, 5, 12]
naive_grouped_fractions([1, 3, 5, 12], True)