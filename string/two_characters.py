from collections import Counter
from itertools import combinations


def solution(s):
    C = Counter(s)
    m = 0
    for pair in combinations(sorted(C, key=C.get, reverse=True), 2):

        T = [c for c in s if c in pair]

        if all(c1 != c2 for c1, c2 in zip(T, T[1:])):
            print(T)
            if len(T) > m:
                m = len(T)
    return m

print(solution('cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc'))
print(solution('muqqzbcjmyknwlmlcfqjujabwtekovkwsfjrwmswqfurtpahkdyqdttizqbkrsmfpxchbjrbvcunogcvragjxivasdykamtkinxpgasmwz'))

print(solution('xyxyx') == 5)
print(solution('xxyy') == 0)
print(solution('abaacdabd') == 4)
print(solution('cobmjdczpffbxputsaqrwnfcweuothoygvlzugazulgjdbdbarnlffzpogdprjxvtvbmxjujeubiofecvmjmxvofejdvovtjulhhfyadr') == 8)
print(solution('cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc') == 8)
print(solution('muqqzbcjmyknwlmlcfqjujabwtekovkwsfjrwmswqfurtpahkdyqdttizqbkrsmfpxchbjrbvcunogcvragjxivasdykamtkinxpgasmwz') == 6)

