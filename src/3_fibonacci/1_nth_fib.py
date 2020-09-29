# Imports
import sys
from os import path
sys.path.append(path.dirname(''))
from src.helpers import execution_time # pylint: disable=import-error

# Given an integer n, find the nth Fibonacci number Fn
# Input: Single integer n, 0 <= n <= 45
# Output: Output Fn


# Naive recursive algorithm
def nth_fib_naive(n):
    if n <= 2:
        return 1
    
    return nth_fib_naive(n-1) + nth_fib_naive(n-1)

# Time complexity mirrors fibonacci sequence 
# execution_time(nth_fib_naive, 25)


# Memoised recursive algorithm
# Create list to save computing values more than once
def nth_fib_memoised(n):
    memo = [0, 1]

    def fib(m):
        if m <= len(memo):
            return memo[m-1]
        else:
            fn = fib(m-1) + fib(m-2)
            memo.append(fn)
            return fn

    return fib(n)

# Only recurses the first time -> linear running time
# execution_time(nth_fib_memoised, 50)


# Non-recursive algorithm
def nth_fib_lookup(n):
    memo = [0] * n
    memo[1] = 1

    for k in range(2, n):
        memo[k] = memo[k-1] + memo[k-2]

    return memo[n-1]

# Performs lookups from bottom up i.e F(0) -> F(n)
# execution_time(nth_fib_lookup, 300)

# Look up with space saver
def nth_fib_lookup_space_save(n):
    if n<=2: return 1

    a,b,c = 0,1,0
    for _ in range(2, n):
        c = a + b
        a = b
        b = c

    return c

# From the lookup we know that we only ever need to know 3 numbers
# execution_time(nth_fib_lookup_space_save, 240)


# Via matrix representation
from numpy import dot

def exponentiate(number, exponent):
    binary = bin(exponent)[2:]

    # Set up vars
    calcs = [1] * len(binary)
    result = 1

    # def calc_indices:
    
    print(result)


def nth_fib_matrix(n):
    if n <= 2: return 1

    matrix =  [[1, 1], [1, 0]]

    # bin_n = str(bin(n))[2:]
    a = matrix
    for _ in range(2, n):
        a = dot(a,matrix)

    print(a)
            

# nth_fib_matrix(100000)
# exponentiate(3, 10)