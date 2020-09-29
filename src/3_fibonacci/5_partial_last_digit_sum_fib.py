# Given two non-negative integers m and n, where m <= n, find the last digit of the sum of Fm, Fm+1... Fn
# Input: Two non-negative integers m and n separated by a space, 0 <= m <= n <= 10^18
# Output: The last digit of Fm, Fm+1... Fn

# Pisano period of 10
def pisano_period_10():
    m = 10
    a, b = [0, 1]

    for i in range(0, m ** 2):
        a,b = b, (a + b) % m

        # Return for start of pisano
        if a == 0 and b == 1:
            return i + 1

def partial_last_digit_sum(input_string, print_result=False):
    # Parse input
    m,n = map(int, input_string.split())
    
    # Find index of period of each
    period = pisano_period_10()
    m_index, n_index = m % period, n % period

    # Initialise sum and memo list
    memo, final_sum = [0] * ((max(m_index, n_index)) + 1), 0

    for i in range(1, max(m_index, n_index) + 1):
        memo[i] = (memo[i-1] + memo[i-2]) % 10 if i > 1 else 1

    final_sum = sum(memo[m_index:n_index+1]) % 10

    if print_result:
        print(final_sum)
    
    return final_sum

# Test 1: 3 7 => 1
partial_last_digit_sum('3 7', True)

# Test 2: 10 10 => 5
partial_last_digit_sum('10 10', True)

# Test 3: 10 200 => 2
partial_last_digit_sum('10 200', True)
