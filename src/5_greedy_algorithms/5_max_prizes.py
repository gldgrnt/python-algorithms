# Represent a positive integer, n, as the sum of as many pairwise distinct positive integers
# Input: a positive integer, n
# Output: a list of pairwise distinct product integers a_1, a_2 ... a_i, a_j, a_k, 1 <= i <= j <= k

def max_prizes(n):
    i, num, leftover = 1, 0, 0

    while True:
        if (i**2 + i) / 2 > n:
            # Take a step back to find the number before it exceeds n
            num = i-1
            # Find leftover to add to last item in results array
            leftover = int(n - (num**2 + num) / 2) 
            break
        elif i == n:
            num = n
            leftover = 0
            break
        # Iterate i
        i += 1
        
    # Create list and add leftover if there is one
    result = list(range(1, num+1))
    result[-1] = result[-1] + leftover if leftover else result[-1]
    # Print as string
    print(f'{len(result)}\n{" ".join([str(item) for item in result])}')

# Test 1: 6 => 3\n1 2 3
max_prizes(6)

# Test 2: 8 => 3\n1 2 5
max_prizes(8)

# Test 3: 2 => 1\n2
max_prizes(2)

# SOLUTION
# 
# Sequence is (i^2 + 1) / 2 for the next 'perfect' number
# so we can find the nearest 'perfect' number and add the difference to the last item in the list
# 
# 'Perfect' numbers:
# 1 : 1
# 3 : 1 2
# 6 : 1 2 3
# 10: 1 2 3 4
# 15: 1 2 3 4 5
# 21: 1 2 3 4 5 6
# 28: 1 2 3 4 5 6 7
# 36: 1 2 3 4 5 6 7 8
