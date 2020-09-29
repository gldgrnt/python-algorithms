# Given integer n, find the last digit of the nth fib number
# Input: Single integer n, 0 <= n <= 10^7
# Output: Last digit of Fn

def nth_fib_last_digit(n):
    # Initialise list of length n + 1 (accounting for zeroindex)
    sequence = [0] * (n+1)

    # Set the first two items
    sequence[0] = 0
    sequence[1] = 1

    # Loop through rest of list
    for i in range(2, len(sequence)):
        # Get the last digit by doing the remainder of the number divided by 10
        sequence[i] = (sequence[i-1] + sequence[i-2]) % 10

    # Print nth item in list
    print(sequence[n])

# Test 1: 3 => 2
nth_fib_last_digit(3)

# Test 2: 331 => 9
nth_fib_last_digit(331)

# Test 3: 327305 => 5
nth_fib_last_digit(327305)