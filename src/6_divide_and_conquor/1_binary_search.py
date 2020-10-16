# Implement binary search
# Input: First line contains an integer n and sequence of n pairwise distinct positive integers in increasing order.
# The second line contains an integer k and k positive integers
# Output: for each item in the second list, output the position of integer in the first list (zeroindexed) or -1 if it's not present
import math

def parse_input(input_string):
    split_input = input_string.split('\n')
    lists = [[int(j) for j in i.split(" ")] for i in split_input]
    return [lists[0][0], lists[0][1:]], [lists[1][0], lists[1][1:]]

def binary_search_recursive(input_string, print_result=True):
    # Parse the input format
    lists = parse_input(input_string)
    base_length, base_list = lists[0]
    search_length, search_list = lists[1]

    # Create recursive method
    def bsr(integer_list, low, high, lookup):
       # Shortcurcuit if lookup can't be found
        if low > high:
            return -1
        # Calculate midpoint
        mid = math.floor((low+high)/2)
        # Check for lookup value and recurse!
        if integer_list[mid] == lookup:
            return mid
        elif integer_list[mid] > lookup:
            return bsr(integer_list, low, mid-1, lookup)
        elif integer_list[mid] < lookup: 
            return bsr(integer_list, mid+1, high, lookup)

    # Call recursive function
    result = [bsr(base_list, 0, base_length-1, item) for item in search_list]
    # Print result
    if print_result:
        print(" ".join([str(item) for item in result]))

    return result

# Test 1: 5 1 5 8 12 13\n5 8 1 23 1 11 => 2 0 -1 0 -1
binary_search_recursive("5 1 5 8 12 13\n5 8 1 23 1 11")