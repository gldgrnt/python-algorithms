# Given a set of points on a line and a set of segments on a line, compute for each point the number of segments that contain this point.
# Input: The first line contains two non-negative integers s and p and the number of segments and the number of points on a line.
# Input: The next line s lines contain two integers a_i and b_i defining the ith segment [a_i, b_i]. The next line contains p integers defining points x_1, x_2 ... x_i
# Output: Output p non-negative integers k_0, k_1 ... k_p-1 where k_i is the number of segments which contain x_i
import random
import math
from timeit import default_timer as timer 

def parse_input(input_string):
    split_input = input_string.split('\n')
    # Seperate variables
    segments_amount, points_amount = [ int(i) for i in split_input[0].split()]
    segments = [[int(i) for i in segs.split()] for segs in split_input[1:-1]]
    points = [int(i) for i in split_input[-1].split()]
    # Return values
    return segments_amount, points_amount, segments, points

# NAIVE SOLUTION
def naive_organising_lottery(input_string):
    # Parse input
    segs_amount, pts_amount, segs, pts = parse_input(input_string)
    result = [None] * pts_amount
    # Count segments containing each point
    for i in range(0, pts_amount):
        count = 0

        for seg in segs:
            if (pts[i] >= seg[0] and pts[i] <= seg[1]):
                count += 1

        result[i] = count

    print(result)

# Test 1: 2 3\n0 5\n7 10\n1 6 11 => 1 0 0
# naive_organising_lottery("2 3\n0 5\n7 10\n1 6 11")

# # Test 2: 1 3\n-10 10\n-100 100 0 => 0 0 1
# naive_organising_lottery("1 3\n-10 10\n-100 100 0")

# # Test 3: 3 2\n0 5\n-3 2\n7 10\n1 6 => 2 0
# naive_organising_lottery("3 2\n0 5\n-3 2\n7 10\n1 6")


# IMPROVED SOLUTION
def improved_organising_lottery(input_string):
    # Parse input
    segs_amount, pts_amount, segs, pts = parse_input(input_string)
    line = list()
    result = [None] * pts_amount
    # Map all segments start and end points to the line
    for seg in segs:
        line.append([seg[0], 'l'])
        line.append([seg[1], 'r'])
    # Map all points onto the line
    for i in range(pts_amount):
        line.append([pts[i], 'p', i])
    # Sort the line by each point
    line = sorted(line, key=lambda point: (point[0], point[1]))
    # Iterate through the line getting the result as we go
    result_count = 0
    inside_seg_count = 0

    for i in range(len(line)):
        curr_pt = line[i]
        if (curr_pt[1] == 'l'):
            inside_seg_count += 1
        elif (curr_pt[1] == 'r'):
            inside_seg_count -= 1
        else:
            result[curr_pt[2]] = inside_seg_count
            result_count += 1

        if (result_count == pts_amount):
            break

    print(result)

# Test 1: 2 3\n0 5\n7 10\n1 6 11 => 1 0 0
# improved_organising_lottery("2 3\n0 5\n7 10\n1 6 11")

# Test 2: 1 3\n-10 10\n-100 100 0 => 0 0 1
# improved_organising_lottery("1 3\n-10 10\n-100 100 0")

# Test 3: 3 2\n0 5\n-3 2\n7 10\n1 6 => 2 0
# improved_organising_lottery("3 2\n0 5\n-3 2\n7 10\n1 6")


# TEST SOLUTIONS
# Helper function to measure the execution time of functions

def execution_time(func, args):
    # Measure time to run func
    start = timer()
    value = func(args)
    stop = timer()
    time = stop - start
    return print(f'Value: {value} in {time}s')

def get_random_amount(seed):
    return random.randint(math.ceil(seed / 2), seed)

def create_input_string(segs_amount, pts_amount, segs, pts):
    input_string = ""
    input_string += f'{segs_amount} {pts_amount}\n'
    
    for seg in segs:
        input_string += f'{seg[0]} {seg[1]}\n'

    for pt in pts:
        input_string += f'{pt} '

    return input_string

def create_data(seed):
    segs_amount = get_random_amount(seed)
    segs = [None] * segs_amount

    for i in range(0, segs_amount):
        a = random.randint(-seed, seed)
        b = random.randint(-seed, seed)
        segs[i] = [min(a,b), max(a,b)]

    pts_amount = get_random_amount(seed)
    pts = [0] * pts_amount 

    for i in range(0, pts_amount):
        pts[i] = random.randint(math.ceil(-seed * 1.5), math.ceil(seed * 1.5))

    return create_input_string(segs_amount, pts_amount, segs, pts)

def run_test():
    data = create_data(50000)
    execution_time(naive_organising_lottery, data)
    execution_time(improved_organising_lottery, data)

# run_test()