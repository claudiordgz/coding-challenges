'''

This initially appears difficult to solve in reasonable time complexity. After further thought,
I think this can be done on O(n) with a few considerations. This is supposed to be an "easy" problem,
so I'll provide some algorithm guidance here.

For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K.
(There is also a special case where both A & B are evenly divisible, giving a sum of 0.)

For any such remainder, there is 1 and only 1 other remainder value which will make a sum divisible by K.

Example: with K of 5, remainder pairs are 1+4 & 2+3. Given the numbers with a remainder of 1, they can't be paired
with ANY of the numbers with remainder 4 (and vice versa). So, for the number of values in the resultant set, choose
the larger of values with remainder 1 vs. values with remainder 4. Choose the larger set of remainder 2 vs remainder 3.

For the special case where remainder is 0, given the set of all values which are individually divisible by K,
they can't be paired with any others. So, at most 1 value which is evenly divisible by K can be added to the result set.

For even values of K, the equal remainder is simular to the 0 case. For K = 6, pairs are 1+5, 2+4, 3+3.

For values with remainder 3, at most one value can be added to the result set.

'''
from fixture import get_testcase
import fileinput

#data = [int(l) for line in fileinput.input() for l in line.split()]

def solution_two(k, numbers):
    counts = [0] * k
    for number in numbers:
        counts[number % k] += 1

    count = min(counts[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(counts[i], counts[k - i])
    if k % 2 == 0:
        count += 1
    return count

def solution(n, k, arr):
    d = {x: [] for x in range(k)}
    for i in range(n):
        d[arr[i] % k].append(arr[i])

    count = 0
    if len(d[0]) > 0:
        count = 1

    # floor division
    s = set([(x, k - x) for x in range(1, k // 2 + 1)])
    for i, j in s:
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1
    return count

def main():
    for t in '120':
        i, o = get_testcase(t)
        clean_data = list(map(int, i))
        n = clean_data[0]
        k = clean_data[1]
        arr = clean_data[2:]
        print(solution(n, k, arr) == int(o[0]))
        print(solution_two(k, arr) == int(o[0]))

if __name__ == '__main__':
    main()
