
from fixture import get_testcase
import math
import functools
import itertools


def has_three(partial_hull):
    return len(partial_hull) > 2


# returns the middle of the last three
# returns ture on success; false otherwise
def remove_middle_of_last_three(partial_hull):
    if not has_three(partial_hull):
        return False

    pos = len(partial_hull)
    del partial_hull[pos - 2]
    return True


def are_last_three_non_right(partial_hull):
    '''
        Determines if last three points reflect a right turn

        if has_three is false, then return false
        return true if last three points on the partial do not
        form a right turn
    '''
    if not has_three(partial_hull):
        return False

    pos = len(partial_hull) - 3
    x1 = partial_hull[pos][0]
    y1 = partial_hull[pos][1]

    x2 = partial_hull[pos+1][0]
    y2 = partial_hull[pos+1][1]

    x3 = partial_hull[pos+2][0]
    y3 = partial_hull[pos+2][1]

    val1 = (x2 - x1)*(y3 - y1)
    val2 = (y2 - y1)*(x3 - x1)
    diff = val1 - val2
    if diff >= 0:
        return True
    return False


def is_valid(grid, n, i, j):
    points = []
    if grid[i][j] != '*':
        if i > 0 and grid[i-1][j] != '*':
            points.append(True)
        if i < n - 1 and grid[i+1][j] != '*':
            points.append(True)
        if j > 0 and grid[i][j - 1] != '*':
            points.append(True)
        if j < n - 1 and grid[i][j + 1] != '*':
            points.append(True)
        return any(points)
    return False


def intersection(L1, L2):
    d = L1[0] * L2[1] - L1[1] * L2[0]
    dx = L1[2] * L2[1] - L1[1] * L2[2]
    dy = L1[0] * L2[2] - L1[2] * L2[0]
    if d != 0:
        x = dx / d
        y = dy / d
        return x, y
    else:
        return False


def make_line(p1, p2):
    a = (p1[1] - p2[1])
    b = (p2[0] - p1[0])
    c = (p1[0] * p2[1] - p2[0] * p1[1])
    return a, b, -c


def calculate_bisector(half_polygon, i):
    def calculate_negative_reciprocal_slope(p1, p2):
        x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]
        slope = (y1 - y2) / (x1 - x2)  if (x1 - x2) != 0 else 0
        reciprocal = 1.0 / slope if slope != 0 else 0
        return - reciprocal

    def calculate_midpoint(p1, p2):
        x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]
        return (x1 + x2) / 2, (y1 + y1) / 2

    p1 = half_polygon[i]
    p2 = half_polygon[i + 1]
    m = calculate_negative_reciprocal_slope(p1, p2)
    x_mid, y_mid = calculate_midpoint(p1, p2)
    b = y_mid - (m * x_mid)
    x_end = 1
    y_end = m * x_end + b
    line = make_line((x_mid, y_mid), (x_end, y_end))
    return line


def intersection_logic(bisectors, i):
    intersect = intersection(bisectors[i], bisectors[i + 1])
    x_intersect = math.ceil(intersect[0])
    y_intersect = math.ceil(intersect[1])
    return x_intersect, y_intersect


def calculate_possible_centers(half_polygon):
    n = len(half_polygon)
    bisectors = [calculate_bisector(half_polygon, i) for i in range(0, n-1, 1)]
    intersects = [intersection_logic(bisectors, i) for i in range(0, len(bisectors)-1)]
    return intersects


def get_half_hull(hull):
    half_hull, start = [hull[0]], 1
    if half_hull[0][1] == hull[1][1]:
        half_hull[0] = hull[1]
        start = 2
    for i in range(start, len(hull) - 1, 2):
        to_append = hull[i] if hull[i][0] > hull[i + 1][0] else hull[i + 1]
        half_hull.append(to_append)
    if hull[-1][1] != half_hull[-1][1]:
        half_hull.append(hull[-1])
    return half_hull


add = lambda x, y: x + y
substract = lambda x, y: x - y


def down(grid, new_radius, row, column):
    return common_up_down(grid, new_radius, row, column, substract, add)


def up(grid, new_radius, row, column):
    return common_up_down(grid, new_radius, row, column, add, substract)


def common_up_down(grid, new_radius, row, column, op1, op2):
    previous_radius = new_radius - 1
    current_row = op1(row, previous_radius)
    side_move = range(1, new_radius, 1)
    move = range(1, new_radius - 1, 1)
    if grid[op1(row, new_radius)][column] == '.':
        for left_right in side_move:
            left_col = grid[current_row][column - left_right] == '.'
            right_col = grid[current_row][column + left_right] == '.'
            if not left_col or \
                    not right_col:
                return False
        if side_move:
            last_col = side_move[-1]
            for m in move:
                new_row = op2(current_row, m)
                if not grid[new_row][column - last_col] == '.' or \
                        not grid[new_row][column + last_col] == '.':
                    return False
        return True
    else:
        return False


def right(grid, new_radius, row, column):
    return grid[row][column + new_radius] == '.'


def left(grid, new_radius, row, column):
    return grid[row][column - new_radius] == '.'


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


def radius_passes_tests(n, grid, row, column, new_radius):
    if column - new_radius < 0 or column + new_radius >= n:
        return False
    if row - new_radius < 0 or row + new_radius >= n:
        return False
    return all((
        up(grid, new_radius, row, column),
        down(grid, new_radius, row, column),
        left(grid, new_radius, row, column),
        right(grid, new_radius, row, column)
    ))


@memoize
def calculate_inscribed_circle_radius(grid, n, center):
    column, row = center[0], center[1]
    radius = 0
    for i in itertools.count(start=1, step=1):
        if radius_passes_tests(n, grid, row, column, i):
            radius = i
        else:
            break
    return radius


def calculate_centers(points):
    hull = convex_hull(points)
    half_hull = get_half_hull(hull)
    centers = list()
    centers.append((int((hull[-1][0] + hull[0][0]) / 2), int((hull[-1][1] + hull[0][1]) / 2)))
    centers.extend(calculate_possible_centers(half_hull))
    return centers


def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    upper_partial = [points[0], points[1]]
    for i in range(2, n):
        upper_partial.append(points[i])
        while has_three(upper_partial) and are_last_three_non_right(upper_partial):
            remove_middle_of_last_three(upper_partial)

    lower_partial = [points[n-1], points[n-2]]
    for i in range(n-3, 0, -1):
        lower_partial.append(points[i])
        while has_three(lower_partial) and are_last_three_non_right(lower_partial):
            remove_middle_of_last_three(lower_partial)

    hull = set()
    for u, l in zip(upper_partial, lower_partial):
        hull.add((u[0], u[1]))
        hull.add((l[0], l[1]))
    hull = sorted(hull, key=lambda x: x[1])
    return hull


def solution(data):
    # orders data in a set of coordinates x,y
    #    x is column
    #    y is row
    n = int(data[0])
    grid = data[1:]
    points = []
    for y in range(n):
        for x in range(n):
            if is_valid(grid, n, x, y):
                points.append([y, x])
    if len(points) < 6:
        return 0
    centers = calculate_centers(points)
    radiuses = [calculate_inscribed_circle_radius(grid, n, center) for center in centers]
    return max(radiuses)


def main():
    for t in '0123456789':
        i, o = get_testcase(t)
        print(solution(i) == int(o[0]))

if __name__ == '__main__':
    main()
