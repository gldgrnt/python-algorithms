# Given two integers n and m, out Fn mod m (the remainder fn divided by m)
# Input: n and m, 2 integers separated by a space, 1 <= n <= 10^18 and 2 <= m <= 10^5
# Output: Fn mod m

# Find pisano period
def pisano_period(m):
    a, b = [0, 1]

    for i in range(0, m ** 2):
        a,b = b, (a + b) % m

        # Return for start of pisano
        if a == 0 and b == 1:
            return i + 1

# Matrix exponentiation of fibonacci
def fibonacci_mod_m(n, m=10):
    if n==1: return 1

    a, b, c = [0, 1, 0]
    # n + 1 for zeroindex
    for i in range(2, n+1):
        c = (a + b) % m
        a = b % m
        b = c
    return c

def nth_fib_mod_m(input_string, print_result=False):
    # Parse string
    n,m = map(int, input_string.split())

    # Find period 
    period = pisano_period(m)

    # Find nth fib mod m of period
    fib_mod_m = fibonacci_mod_m(n % period, m)
    
    if print_result:
        print(f'nth fibonnaci mod m is: {fib_mod_m}')

    return fib_mod_m

# Test 0: 2015 3 => 1
nth_fib_mod_m('2015 3', True)

# Test 1: 239 1000 => 161
nth_fib_mod_m('239 1000', True)

# Test 2: 2816213588 239 => 151
nth_fib_mod_m('2816213588 239', True)