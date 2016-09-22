

def sequence(N):
    return [[] for _ in range(N)]


def get_sequence(n, last, N):
    return (n ^ last) % N


def test_sequence():
    print(len(sequence(5)) == 5)
    print(len(sequence(6)) == 6)
    print(len(sequence(0)) == 0)


def test_get_sequence():
    print(get_sequence(0, 0, 2) == 0)
    print(get_sequence(1, 0, 2) == 1)
    print(get_sequence(0, 0, 2) == 0)
    print(get_sequence(1, 0, 2) == 1)


def solution(input):
    N = input[0]
    data = input[2:]
    i, s, last_ans = 0, sequence(N), 0
    while i < input[1]:
        q, x, y = data[3*i], data[3*i+1], data[3*i+2]
        seq_to_select = get_sequence(x, last_ans, N)
        if q == 1:
            s[seq_to_select].append(y)
        else:
            last_ans = s[seq_to_select][y % len(s[seq_to_select])]
            yield last_ans
        i += 1


def read_file(filename):
    f = open(filename, "r")
    n = [int(i) for i in f.read().split()]
    f.close()
    return n


def test_0():
    input = read_file('input_0.txt')
    output = read_file('output_0.txt')
    print([i for i in solution(input)] == output)

def test_1():
    input = read_file('input_1.txt')
    output = read_file('output_1.txt')
    print([i for i in solution(input)] == output)

test_sequence()
test_get_sequence()
test_0()
