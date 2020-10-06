# Given a set of n seegments {[a_0, b_0], [a_1, b_1]... [a_n-1, b_n-1]} with integer coordinates on a line
# find the minimum number of points, m, such that each segment contains at least 1 point. a_i <= x <= b_i
# Input: First line is n number of segments, the following lines containing two integers a_i and b_i defining
# the endpoints of the ith segment
# Output: Minimum number of points m on the first line, followed by a list of the integer coordinates of each point

def parse_input(input_string):
    split_input = input_string.split('\n')
    return split_input[0], [[int(j) for j in i.split()] for i in split_input[1:]]

def collect_signatures(input_string):
    amount_input, coords_input = parse_input(input_string)

    def find_segment(coords, segments=[]):
        if len(coords) == 0:
                print(f'{len(segments)}\n{" ".join([str(item) for item in segments])}')
        else:
            # Find lowest ending coord
            segments += [sorted(coords, key=lambda item: item[1])[0][1]]
            # Filter out items that contain the integer
            filtered_coords = list(filter(lambda item: item[0] > segments[-1] or segments[-1] > item[1],  coords))
            find_segment(filtered_coords, segments)

    # Recurse!
    find_segment(coords_input)

# Test 1: 3\n1 3\n2 5\n3 6 => 1\n3
collect_signatures("3\n1 3\n2 5\n3 6")
print("\n")
# Test 2: 4\n4 7\n1 3\n2 5\n5 6 => 2\n3 6
collect_signatures("4\n4 7\n1 3\n2 5\n5 6")