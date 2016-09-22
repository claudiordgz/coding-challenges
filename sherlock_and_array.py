import fileinput


def solution(arr):
    i, j = 0, len(arr) - 1
    _sum = 0
    while i != j:
        if _sum >= 0:
            _sum -= arr[j]
            j -= 1
        else:
            _sum += arr[i]
            i += 1
    return 'YES' if _sum == 0 else 'NO'


if __name__ == '__main__':
    print(solution([1,2,3]))
    print(solution([1,2,3,3]))