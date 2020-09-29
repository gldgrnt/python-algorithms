# Maximum pairwise product
# Input: 1st line: N, 2nd line: A sequence of N non-negative intigers
# Output: The macimium value that can be obtained by multiplyiing two different elements from the sequence
# Contraints: Min 2 numbers, numbers between 0 and 20000
import sys
from timeit import default_timer as timer

# Get inputs from file

def max_pairwise_product_1():
    # Get input
    file = open("src/solutions/2_max_pairwise_product/input.txt", "r").read()
    input = file.strip()

    # Split up input
    split_input = input.split()
    n = int(split_input[0])
    a = split_input[1:]

    # Get maximum ints in the array
    product = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, int(a[i]) * int(a[j]))

    # print(f'{product} {end - start}')
    return product

max_pairwise_product_1()