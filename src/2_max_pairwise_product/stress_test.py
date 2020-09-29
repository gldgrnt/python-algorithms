# Stress testing of fast and slow algorithms
import random
from input import create_input
from solution_1 import max_pairwise_product_1
from solution_2 import max_pairwise_product_2

## Function to stress test solutions
# @param n length of number array
# @param m upper limit of randomly generated number
def stress_test(n, m):
    while True:
        # Create new random input file
        random_n = random.randint(2, n)
        create_input(random_n, m)

        # Find solutions and compare
        product_1 = max_pairwise_product_1()
        product_2 = max_pairwise_product_2()

        # Print results
        case = f'{random_n}, {m}'
        if product_1 == product_2:
            print(f'{case}: OK')
        else: 
            print(f'{case}: Not OK')
            break

stress_test(10000, 1000000)
