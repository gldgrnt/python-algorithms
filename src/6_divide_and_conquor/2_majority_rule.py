# Check whether an input sequence contains a majority element
# Input: First line contains an integer, n, and the next line contains a sequence of integers, a_1, a_2 ... a_n
# Output: Output 1 if the sequence contains an elements that occurs stricly more than n/2 times, and output 0 if not
import math

def parse_input(input_string):
    split_input = input_string.split('\n')
    n, seq = split_input[0], [int(i) for i in split_input[1].split()]
    return n, seq

def majority_element(input_string):
    number, sequence = parse_input(input_string)

    # Helper function to compare for the most frequent number if both sides give different values
    def compare_numbers(int_list, left_num, right_num):
        left_num_freq, right_num_freq = 0,0

        # Increment respective frequency if number is the same
        for integer in int_list:
            if (integer == left_num):
                left_num_freq += 1
            if (integer == right_num):
                right_num_freq += 1

        # Return the most frequent or the left most element
        if left_num_freq >= right_num_freq:
            return left_num
        else:
            return right_num

    # Create recursive function
    def maj_el(integer_list, low, high):
        # Find midpoint to split the list
        mid = math.floor((low+high)/2)

        # Handle base case
        if (low == high):
            return integer_list[low]
        
        # Recursively call function on each side
        left = maj_el(integer_list, 0, mid)
        right = maj_el(integer_list, mid+1, high)

        if (left == right):
            return left
        else: 
            return compare_numbers(integer_list, left, right)

    # Check for final majority as recursive functions returns left most element if there's no majority
    majority = maj_el(sequence, 0, len(sequence)-1)
    frequency = 0
    # Loop through element
    for integer in sequence:
        if integer == majority:
            frequency += 1
    # Check if greater than n/2
    if frequency > int(number)/2:
        return print(1)
    else:
        return print(0)


# Test 1: 5\n2 3 9 2 2 => 1
majority_element("5\n2 3 9 2 2")

# Test 2: 4\n1 2 3 4 => 0
majority_element("4\n1 2 3 4")

# Test 3: 4\n1 2 3 1 => 0
majority_element("4\n1 2 3 1")