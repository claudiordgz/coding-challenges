
sample_input = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0]
]

second_input = [
    [ 0, 6,-7, 1, 6, 3],
    [-8, 2, 8, 3,-2, 7],
    [-3, 3,-6,-3, 0,-6],
    [ 5, 0, 5,-1,-5, 2],
    [ 6, 2, 8, 1, 3, 0],
    [ 8, 5, 0, 4,-7, 4],
]

def get_hourglass_center(n, m):
    i, j = 1, 1
    while i < n:
        while j < m:
            yield (i,j)
            j += 1
        i, j = i+1, 1

def get_hourglass(input, x, y):
    return (
        input[x - 1][y - 1],
        input[x - 1][y],
        input[x - 1][y + 1],
        input[x][y],
        input[x + 1][y - 1],
        input[x + 1][y],
        input[x + 1][y + 1],
    )

def get_max(input):
    n, m = len(input[1:-1]) + 1, len(input[0][1:-1]) + 1
    return max(sum(get_hourglass(input, i, j)) for i, j in get_hourglass_center(n, m))

def solution(input):
    if not input: return
    return get_max(input)


print(solution(sample_input) == 19)
print(solution(second_input) == 25)
solution([])