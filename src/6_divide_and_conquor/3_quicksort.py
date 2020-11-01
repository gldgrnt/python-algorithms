# Implement quicksort
# Input: First line contains an integer n, and the second line is a sequence of integers a_0, a_1... a_n
# Output: The sequence sorted in increasing order

def parse_input(input_string):
    split_input = input_string.split('\n')
    n, seq = split_input[0], [int(i) for i in split_input[1].split()]
    return n, seq

def quicksort(input_string):
    number, sequence = parse_input(input_string)

    # Swap helper function
    def swap(a, b):
        hold = sequence[b]
        sequence[b] = sequence[a]
        sequence[a] = hold

    # Partition function to sort around a pivot
    def partition(low, high):
        # Take the pivot as the element at the high point
        pivot = sequence[high]
        i = low
        j = high
        # Loop through and sort elements around the pivot
        while True:
            if sequence[i] > pivot:
                j -= 1
                if i < j:
                    swap(i,j)
                    swap(j, j+1)
                else:
                    swap(i, j+1)
            else:
                i += 1
            # Break from loop
            if i >= j:
                break
        # Return index of partition
        return i
                
    def qs(low, high):
        if low < high:
            p = partition(low, high)
            qs(low, p - 1)
            qs(p + 1, high)
        
    qs(0, len(sequence) - 1)
    # Return the sequence
    return print(sequence)

# Test 1: 5\n2 3 9 2 2 =>  2 2 2 3 9
quicksort("5\n2 3 9 2 2")