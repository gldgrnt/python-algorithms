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

def closest_points(input_string):
    points_number, points = parse_input(input_string)
    # Split points down the line x = 0

    print(Point.distance_between_points(points[0], points[1]))

# Test 1: 2\n0 0\n3 4 => 5.0
closest_points("2\n0 0\n3 4")