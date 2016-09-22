import fileinput
from fixture import get_testcase
import itertools


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


def radius_passes_tests(n, grid, row, column, new_radius):
    if column - new_radius < 0 or column + new_radius >= n:
        return False
    if row - new_radius < 0 or row + new_radius >= n:
        return False
    return all((
        left(grid, new_radius, row, column),
        right(grid, new_radius, row, column),
        up(grid, new_radius, row, column),
        down(grid, new_radius, row, column)
    ))


def calculate_inscribed_circle_radius(grid, n, center):
    column, row = center[0], center[1]
    radius = 0
    if grid[row][column] == '.':
        for i in itertools.count(start=1, step=1):
            if radius_passes_tests(n, grid, row, column, i):
                radius = i
            else:
                break
    return radius


def solution(data):
    # orders data in a set of coordinates x,y
    #    x is column
    #    y is row
    n = int(data[0])
    grid = data[1:]
    radius = []
    for y in range(n):
        for x in range(n):
            r = calculate_inscribed_circle_radius(grid, n, (x, y))
            radius.append(r)
    return max(radius)


def main():
    for t in range(0, 13):
        i, o = get_testcase(t)
        print(solution(i) == int(o[0]))

if __name__ == '__main__':
    main()

'''
data = [line.rstrip('\n') for line in fileinput.input()]
print(solution(data))
'''