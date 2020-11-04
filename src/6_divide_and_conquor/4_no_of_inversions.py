# Count the number of inversions in a given sequence
# Input: First line contains an integer n, and the second line is a sequence of integers a_0, a_1... a_n
# Output: the number of inversions
import math

def parse_input(input_string):
    split_input = input_string.split('\n')
    n, seq = int(split_input[0]), [int(i) for i in split_input[1].split()]
    return n, seq

def no_of_inversions(input_string):
    n, sequence = parse_input(input_string)

    def merge_lists(left, right, inversions=0):
        result_length = len(left) + len(right)
        result = [None] * result_length
        l_pointer,r_pointer,invs = 0,0,0
        # Loop through lists
        for i in range(0, result_length):
            # Handle base case
            if len(left) <= l_pointer and len(right) <= r_pointer:
                break
            # Comparisons
            if len(left) <= l_pointer and not len(right) <= r_pointer:
                result[i] = right[r_pointer]
                r_pointer += 1
            elif len(right) <= r_pointer and not len(left) <= l_pointer:
                result[i] = left[l_pointer]
                l_pointer += 1
            elif left[l_pointer] < right[r_pointer]:
                result[i] = left[l_pointer]
                l_pointer += 1
            else:
                result[i] = right[r_pointer]
                r_pointer += 1
                # Increment inversions IFF a number on the RHS is smaller than the number on the LHS
                invs += 1
        # Return sorted list'
        return result, invs

    def mergesort(list_to_sort, length):
        if length == 1:
            return list_to_sort, 0

        # Find the midpoint
        mid = math.ceil(length/2)
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        # Divide and conquer!
        left_sorted, l_inversions = mergesort(left, len(left))
        right_sorted, r_inversions = mergesort(right, len(right))
        inversions = l_inversions + r_inversions

        return merge_lists(left_sorted, right_sorted, inversions)

    sorted_sequence, inversions = mergesort(sequence, n)
    print(inversions)
    return sorted_sequence

# Test 1: 5\n2 3 9 2 9 => 2
no_of_inversions("5\n2 3 9 2 9")