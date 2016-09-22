import fileinput

data = [int(l) for line in fileinput.input() for l in line.split()]

n = data[0]
arr = data[1:]


def print_array(arr):
    print(' '.join(map(str, arr)))


def insertion_sort(l):
    for i in range(len(l))[1:]:
        k, j = l[i], i - 1
        while j >= 0 and l[j] < k:
            l[j + 1], j = l[j], j - 1
        l[j + 1] = k
        print_array(arr)


insertion_sort(arr)