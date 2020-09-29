# Given two integers a and b, find their lowest common multiple
# Input: Two integers given on the same line separated by a space, 1 <= a,b <= 2 * 10^9
# Output: The least common multiple
from timeit import default_timer as timer
import math

def lcm(input_string):
    # Parse string
    a,b = map(int, input_string.split())

    # Find known common multiple
    known_cm = a * b
    smallest = min(a, b)
    largest = max(a, b)
    lcm = known_cm

    # Loop through backwards in steps of -a to b
    for i in range(known_cm, largest, -smallest):
        if i != known_cm and i % largest == 0:
            lcm = i

    print(lcm)

# Optimised version using gcd
# lcm = a * b / gcm(a,b)
def lcm_fast(input_string):
    # Parse string
    a,b = map(int, input_string.split())

    # Use inbuilt gcm function 
    lcm = (a * b) / math.gcd(a,b)
    return print(round(lcm))
    

# Test 1: 6 8 => 24
lcm_fast('6 8')

# Test 2: 28851538 1183019 => 1933053046
lcm_fast('28851538 1183019')