# Count the number of inversions in a given sequence
# Input: First line contains an integer n, and the second line is a sequence of integers a_0, a_1... a_n
# Output: the number of inversions

def parse_input(input_string):
    split_input = input_string.split('\n')
    n, seq = split_input[0], [int(i) for i in split_input[1].split()]
    return n, seq

def no_of_inversions(input_string):