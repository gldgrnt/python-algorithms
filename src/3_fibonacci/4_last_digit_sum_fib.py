# Given an intenger n, find the last digit sum of Fn
# Input: n, 0 <= n <= 10^14
# Output: Last digit sum

# Pisano period of 10
def pisano_period_10():
    m = 10
    a, b = [0, 1]

    for i in range(0, m ** 2):
        a,b = b, (a + b) % m

        # Return for start of pisano
        if a == 0 and b == 1:
            return i + 1

def last_digit_sum_fib(n, print_result=False):
    # Find remainder from pisano period of 10
    # Last digit is the same as Fn mod 10
    index = n % pisano_period_10()
    sum, memo = 0, [0] * (index + 1)

    for i in range(1, index + 1):
        memo[i] = (memo[i-1] + memo[i-2]) % 10 if i > 1 else 1
        
        if (n <= 3 and i == index) or (index > 3 and ((index - 3) - i) % 3 == 0):
            sum = (sum + (2 * memo[i]) if i > 1 else memo[i]) % 10

    if print_result:
        print(sum)

    return sum

# Test 1: 3 => 4
last_digit_sum_fib(3, True)

# Test 2: 100 => 5
last_digit_sum_fib(100, True)