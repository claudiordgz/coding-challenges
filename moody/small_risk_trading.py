from fixture import get_testcase, read_raw


def get_value(p, x, y):
    profit, loss = p * x, (1 - p) * y
    return profit - loss


def solution(data):
    n, k = list(map(int, data[0].split()))
    to_number = lambda x: list(map(float, x.split()))
    p_arr, x_arr, y_arr = to_number(data[1]), to_number(data[2]), to_number(data[3])
    values = [get_value(p,x,y) for p, (x, y) in zip(p_arr, zip(x_arr, y_arr))]
    sorted_values = sorted(filter(lambda x: x >= 0, values), reverse=True)
    acc = 0
    for i, n in enumerate(sorted_values):
        acc += n
        if i + 1 == k: break
    return round(acc, 2)


if __name__ == '__main__':
    for t in '01':
        i, o = get_testcase(t, read_as=read_raw, folder_name='testcases/01')
        print(format(solution(i), '.2f'))
        print(format(float(o[0]), '.2f'))
        print(format(solution(i), '.2f') == format(float(o[0]), '.2f'))
