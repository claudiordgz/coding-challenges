import fileinput

data = [int(l) for line in fileinput.input() for l in line.split()]


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


def solution(input):
    print(' '.join([str(i) for i in shift(input[2:], input[1])]))


solution(data)