# Given two sequence a_1, a_2 ... a_n (a_i profit of ith ad) and b_1, b_2 ... b_n (b_i is the average number of clicks per day of a given slot) 
# partiton the sequences into pairs (a_i, b_j) such that the sum of their products is maximised

def parse_input(input_string):
    split_input = input_string.split("\n")
    amount = int(split_input[0])
    
    if amount < 2:
        profit, slots =  [[int(i)] for i in split_input[1:]]
        return amount, profit, slots 
    else: 
        profit, slots = [[int(j) for j in i.split()] for i in split_input[1:]]
        return amount, profit, slots

def max_ad_revenue(input_string, print_result=False):
    # Parse input
    amount, profit, slots = parse_input(input_string)

    # Combine and multiply adjacent indeces, step 2 each time
    combined = sorted(profit + slots, reverse=True)
    revenue = sum([combined[i] * combined[i+1] for i in range(0, amount*2, 2)])

    if print_result:
        print(f'Max revenue: {revenue}')

    return revenue

# Test 1: 1\n23\n39 => 897
max_ad_revenue("1\n23\n39", True)

# Test 2: "3\n1 3 -5\n-2 4 1" => 23
max_ad_revenue("3\n1 3 -5\n-2 4 1", True)