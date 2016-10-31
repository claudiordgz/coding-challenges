from fixture import get_testcase, read_raw


def solution(m, a):
    """ Find two elements in list who sum to m

    :param m: the total we are searching for
    :param a: the list of integers
    :return: two flavors tuple
    """
    seen = {}
    for i, cost in enumerate(a, 1):
        try:
            c1, c2 = (seen[m - cost], i)
            return c1, c2
        except KeyError:
            seen[cost] = i


def main():
    for t in ['00']:
        i, o = get_testcase(t, read_as=read_raw, folder_name='testcases/binary_search_ice_cream_parlor')
        trips = int(i[0])
        data = i[1:]
        for i in range(trips):
            j = i*3
            m = int(data[j])
            #c = int(data[j+1])
            a = list(map(int, data[j + 2].split()))
            c1, c2 = solution(m, a)
            print(c1, c2)

if __name__ == '__main__':
    main()
