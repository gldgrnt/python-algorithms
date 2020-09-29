# Find the minimum number of coins needed to change the input integer into denominations of 1,5 and 10
# Input: A single integer m, 1 <= m <= 10^3
# Output: The minimum number of coins with denominations that changes m
from math import floor

# Recursive solution
def min_coins_recusive(input, print_result=False):
    a, b, c = input, [1, 5, 10], 0

    def make_change(remainder, denominations, total):
        if len(denominations) < 1:
            if print_result:
                print(f'Min coins recursive: {total}')
            return total
        else:    
            calculate_new = remainder / max(denominations) >= 1
            # Use ternary to be succint
            new_total = total + floor(remainder / max(denominations)) if calculate_new else total
            new_remainder = remainder % max(denominations) if calculate_new else remainder
            # Call function with new inputs
            make_change(new_remainder, denominations[:-1], new_total)

    # Call function
    make_change(a, b, c)

# Test 1: 2 => 2
min_coins_recusive(2, True)

# Test 2: 28 => 6
min_coins_recusive(28, True)


# Iterative solution
def min_coins_iterative(input, print_result=False):
    # Denominations [high -> low]
    remainder, denominations, total  = input, [10, 5, 1], 0

    for coin in denominations:
        total += floor(remainder / coin)
        remainder = remainder % coin

    if print_result:
        print(f'Min coins iterative: {total}')

    return total

# Test 1: 2 => 2
min_coins_iterative(2, True)

# Test 2: 28 => 6
min_coins_iterative(28, True)