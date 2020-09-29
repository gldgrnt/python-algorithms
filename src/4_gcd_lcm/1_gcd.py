# Given two integers a and b, find their greatest common divisor
# Input: Two integers given on the same line separated by a space, 1 <= a,b <= 2 * 10^9
# Output: GCD(a,b)
from timeit import default_timer as timer

def gcd(input_string):
    # Parse string
    a,b = map(int, input_string.split())

    max_divisor = min(a, b)
    gcd = 1
    
    # Add 1 to be inclusive
    for i in range(1, max_divisor + 1):
        if int(a) % i == 0 and int(b) % i == 0:
            gcd = i
    
    print(gcd)

# Optimised version of the algorithm using Euclidean theorem
def gcd_fast(input_string):
    # Parse string
    a,b = map(int, input_string.split())
    
    if min(a,b) == 0:
        return print(max(a, b))
    else: 
        c = max(a, b) % min(a, b)
        return gcd_fast(f'{c} {min(a,b)}')

# Test 1: 18 35 => 1
gcd_fast('18 35')

# Test 2: 28851538 1183019 => 17657
gcd_fast('28851538 1183019')