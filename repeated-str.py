'''
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.
'''


def solution(sentence, N, char):
    total_chars = len(sentence)
    remainder, total_strings = N % total_chars, N // total_chars
    last_count = sentence[:remainder].count(char) if remainder != 0 else 0
    return (sentence.count(char) * total_strings) + last_count

if __name__ == '__main__':
    print(solution('a', 1000000000000, 'a') == 1000000000000)
    print(solution('aba', 10, 'a') == 7)
