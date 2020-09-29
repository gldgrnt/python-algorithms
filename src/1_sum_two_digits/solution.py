# Sum of two digits
# Input: a and b, two single digit numbers on the same line separated by a comma
# Output: the sum of a and b
# Constraints: 0 <= a <= 9
import sys

def sum_two_digits():
    # Get input from user
    digits_input = sys.stdin.readline()

    # Split inputs and add
    digits = digits_input.split()
    result = int(digits[0]) + int(digits[1])

    # Print result
    print(result)

sum_two_digits()