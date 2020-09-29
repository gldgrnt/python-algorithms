# Help a thief find the most valuable combination of loot
# Input: First line contains number of items and maximum weight of knapsack, n and W, separated by a space
# Input: Following lines contain values and weights of the items, v_i  and w_i, separated by a space
# Output: The maximal value of the items in the knapsack, e.g 10.6667

def parse_input(input_string): 
    split_input = input_string.split('\n')
    amount_input, max_weight_input = map(int, split_input[0].split())
    items_input = [[int(j) for j in i.split()] for i in split_input[1:]]
    # Return parts of input string
    return [amount_input, max_weight_input, items_input]

# Recursive
def maximal_loot_recursive(input_string, print_result=False):
    # Parse the input
    amount_input, max_weight_input, items_input = parse_input(input_string)

    # Sort items by largest value to weight ratio
    sorted_items_input = sorted(items_input, key=lambda item: item[0]/item[1], reverse=True)

    # Define recursive function to fill bag
    def fill_bag(remaining_weight, sorted_items, bag_value=0):
        if remaining_weight == 0 or len(sorted_items) == 0:
            if print_result:
                print(f'Maximal loot recursive: {bag_value}')
            return bag_value
        else:
            # Check if there's enough room
            enough_weight = remaining_weight >= sorted_items[0][1]
            # Find remaining weight and bag value
            bag_value = bag_value + sorted_items[0][0] if enough_weight else sorted_items[0][0] * (remaining_weight / sorted_items[0][1])
            remaining_weight = remaining_weight - sorted_items[0][1] if enough_weight else 0
            # Recurse!
            fill_bag(remaining_weight, sorted_items[1:], bag_value)

    # Call recursive function
    fill_bag(max_weight_input, sorted_items_input)
        

# Test 1: 3 50\n60 20\n100 50\n120 30 => 180.000
maximal_loot_recursive('3 50\n60 20\n100 50\n120 30', True)

# Test 2: 1 10\n500 30 => 166.6667
maximal_loot_recursive('1 10\n500 30', True)


# Iterative
def maximal_loot_iterative(input_string, print_result=False):
    # Parse the input
    amount, remaining_weight, items = parse_input(input_string)
    bag_value = 0

    # Sort items
    sorted_items = sorted(items, key=lambda item: item[0]/item[1], reverse=True)

    # Loop through items
    for i in range(0, len(sorted_items)):
        if remaining_weight == 0:
            break

        if remaining_weight >= sorted_items[i][1]:
            remaining_weight -= sorted_items[i][1]
            bag_value += sorted_items[i][0]
        else: 
            # Find the value of the amount that can fit in the bag
            bag_value += (1 - (sorted_items[i][1] - remaining_weight)/ sorted_items[i][1]) * sorted_items[i][0]
            remaining_weight = 0
    
    if print_result:
        print(f'Maximal loot iterative: {bag_value}')
    return bag_value
            
    
# Test 1: 3 50\n60 20\n100 50\n120 30 => 180.000
maximal_loot_iterative('3 50\n60 20\n100 50\n120 30', True)

# Test 2: 1 10\n500 30 => 166.6667
maximal_loot_iterative('1 10\n500 30', True)