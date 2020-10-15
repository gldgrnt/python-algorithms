# Compose the largest number from a set of integers
# Input: First line is n, the number of integers, with the second line contains integers from a_1 to a_n
# Output: The largest number that can be composed from all input integers

def parse_input(input_string):
    split_input = input_string.split('\n')
    return split_input[0], [int(i) for i in split_input[1].split()]

def is_greater_or_equal_by_digit(int_1, int_2):
    # Check for the int with smallest number of digits
    min_digits = min(len(str(int_1)), len(str(int_2)))
    # Convert to integers of min_digit length
    int_1_min, int_2_min = int(str(int_1)[:min_digits]), int(str(int_2)[:min_digits])
    # Return comparison
    return int_1_min >= int_2_min

def max_salary(input_string):
    n, integers = parse_input(input_string)
    # Recursive function to return result
    def create_max_salary(integers_list, result_list=[]):
        if not integers_list:
            print(''.join([str(integer) for integer in result_list]))
        else:
            max_digit, index = 0, 0
            # Loop through and take out biggest
            for idx, value in enumerate(integers_list):
                if is_greater_or_equal_by_digit(value, max_digit):
                    max_digit = value
                    index = idx
            # Remove index and to results list
            new_result = result_list + [max_digit]
            new_integers_list = integers_list[:index] + integers_list[index+1:]
            # Recurse!
            return create_max_salary(new_integers_list, new_result)

    # Use recursive function
    salary = create_max_salary(integers) 

# Test 1: 2\n21 2 => 221
max_salary("2\n21 2")

# Test 2: 5\n9 4 6 1 9 => 99641
max_salary("5\n9 4 6 1 9")

# Test 3: 3\n23 39 92 => 923923
max_salary("3\n23 39 92")