# Given a set of points on a line and a set of segments on a line, compute for each point the number of segments that contain this point.
# Input: The first line contains two non-negative integers s and p and the number of segments and the number of points on a line.
# Input: The next line s lines contain two integers a_i and b_i defining the ith segment [a_i, b+i]. The next line contains p integers defining points x_1, x_2 ... x_i
# Output: Output p non-negative integers k_0, k_1 ... k_p-1 where k_i is the number of segments which contain x_i

# 2 3
# 0 5
# 7 10
# 1 6 11

def parse_input(input_string):
    split_input = input_string.split('\n')
    # Seperate variables
    segments_amount, points_amount = [ int(i) for i in split_input[0].split()]
    segments = [[int(i) for i in segs.split()] for segs in split_input[1:-1]]
    points = [int(i) for i in split_input[-1].split()]
    # Return values
    return segments_amount, points_amount, segments, points

def organising_lottery(input_string):
    # Parse input
    segs_amount, pts_amount, segs, pts = parse_input(input_string)

    

parse_input("2 3\n0 5\n7 10\n1 6 11")