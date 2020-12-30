# Given n points on a plane, find the smallest distance between a pair of two different point.
# Input: The first line contains the number n of points, Each of the following n lines defines a point (x_i, y_i)
# Output: The minimum distance. Absolute difference between answer and optimat value should be 10^-3
import math

class Point:
    def __init__(self, pt_string):
        x,y = [int(i) for i in pt_string.split(' ')]
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} {self.y}'

    @staticmethod
    def distance_between_points(pt1, pt2):
        x_diff_sqrd = (pt1.x - pt2.x)**2
        y_diff_sqrd = (pt1.y - pt2.y)**2
        return math.sqrt(x_diff_sqrd + y_diff_sqrd)

def parse_input(input_string):
    split_input = input_string.split('\n')
    # Seperate variables
    points_number = int(split_input[0])
    points = [Point(pt_strings) for pt_strings in split_input[1:]]
    # Return values
    return points_number, points

# This method is somewhat constant because we only ever do a max of 6 calculations 
def find_shortest_distance(pts):
    distance = 1000000
    amount = len(pts)

    if (amount < 2):
        # Return large number is the same as returning nothing in this case
        return distance

    for i in range(amount - 1):
        for j in range(i + 1, amount):
            d = Point.distance_between_points(pts[i], pts[j])
            distance = min(d, distance)

    return distance


def closest_points(input_string):
    points_number, points = parse_input(input_string)
    
    def cp(pts):
        # Get the closest for a small number of points
        if (len(pts) <= 4):
            return find_shortest_distance(pts)

        # Sort the points by x coordinate
        sorted_pts = sorted(pts, key=lambda pt: pt.x)
        center = math.ceil((len(pts) + 1) / 2)

        # Find the shortest distance each side
        shortest_left = cp(pts[:center])
        shortest_right = cp(pts[center:])

        # If we're unlucky, the shortest distance between two points is split between both sides
        # Find the shortest distance in the intersection center +- shortest/2 so far
        shortest = min(shortest_left, shortest_right)
        inter_left = center - (shortest / 2)
        inter_right = center + (shortest / 2)

        # Filter out all points that aren't in the intersection (and keep them in order)
        intersection_pts = [pt for pt in pts if pt.x >= inter_left or pt.x <= inter_right]
        # In this case we can just call find_shortest_distance() but if we had a large number of points
        # in the intersection we'd have to call a slightly difference method that finds the 
        # shortest distance in steps i.e iteratively call find_shortest_distance() on blocks of 3 for example
        shortest_inter = find_shortest_distance(intersection_pts) 

        # Return the min of all shortest distances calculated
        return min(shortest, shortest_inter)

    result = cp(points)
    print(result)


# Test 1: 2\n0 0\n3 4 => 5.0
closest_points("2\n0 0\n3 4")

# Test 2: 4\n7 7\n1 100\n4 8\n7 7 => 0.0
closest_points("4\n7 7\n1 100\n4 8\n7 7")

# Test 3: 11\n4 4\n-2 -2\n-3 -4\n-1 3\n2 3\n-4 0\n1 1\n-1 -1\n3 -1\n-4 2\n-2 4 => 1.14213
closest_points("11\n4 4\n-2 -2\n-3 -4\n-1 3\n2 3\n-4 0\n1 1\n-1 -1\n3 -1\n-4 2\n-2 4")