from fixture import get_testcase, read_raw


def contains(hash_table, ransom):
    for word in ransom:
        if word in hash_table and hash_table[word] > 0:
            hash_table[word] -= 1
        else:
            return False
    return True


def ransom_note(magazine, ransom):
    hash_table = {}
    for key in magazine:
        if key not in hash_table:
            hash_table[key] = 1
        else:
            hash_table[key] += 1
    return contains(hash_table, ransom)


def solution(data):
    m, n = map(int, data[0].split(' '))
    magazine = data[1].split(' ')
    ransom = data[-1].split(' ')
    return "Yes" if ransom_note(magazine, ransom) else "No"


def main_hr():
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if (answer):
        print("Yes")
    else:
        print("No")


def main():
    for t in ['00', '01', '02']:
        i, o = get_testcase(t, read_as=read_raw, folder_name='testcases/hash_tables')
        print(solution(i) == o[0])


if __name__ == '__main__':
    main()