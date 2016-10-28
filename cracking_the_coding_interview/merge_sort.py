from itertools import combinations
from random import randrange
from unittest import TestCase
import unittest

def merge_and_count_inversions(seq, start, middle, end):
    """Merge two adjacent sorted sub-sequences of seq and count
    inversions.

    Changes sequence in place
    :param seq: full sequence to sort
    :param start: index of beginning of first sorted subsequence
    :param middle: end of first, beginning of second sorted subsequence
    :param end: end of second sorted subsequence
    :return: number of inversions (cases where i < j, but seq[i] > seq[j]).
    """
    assert 0 <= start < middle < end <= len(seq)
    inversions = 0
    temp = []
    i = start
    j = middle
    while i < middle and j < end:
        if seq[i] <= seq[j]:
            temp.append(seq[i])
            i += 1
        else:
            temp.append(seq[j])
            j += 1
            inversions += middle - i
    if j == end:
        # Second subsequence is complete: process remainder of first.
        temp.extend(seq[i:middle])
    else:
        # First subsequence is complete: no need to process
        # remaininder of second, since it does not move.
        pass
    # Insert sorted results into original sequence.
    seq[start:start+len(temp)] = temp
    return inversions


def sort_and_count(seq, start, end):
    if end - start < 2:
        return 0
    middle = (start + end) // 2
    return (sort_and_count(seq, start, middle)
            + sort_and_count(seq, middle, end)
            + merge_and_count_inversions(seq, start, middle, end))


def sort_and_count_inversions(seq):
    """ Sort a sequence and count inversions.
        Sequence is sorted in place
    :param seq: seq -- a sequence
    :return: number of inversions (cases where i < j, but seq[i] > seq[j]).
    """
    return sort_and_count(seq, 0, len(seq))



def main():
    a = [1, 1, 1, 2, 2]
    b = [2, 1, 3, 1, 2]
    print(sort_and_count_inversions(a))
    print(sort_and_count_inversions(b))


class TestSortAndCount(TestCase):
    def check(self, seq):
        expected = sum(j < i for i, j in combinations(seq, 2))
        found = sort_and_count_inversions(seq)
        self.assertEqual(expected, found)
        self.assertEqual(seq, sorted(seq))

    def runTest(self):
        self.check([])                    # empty sequence
        self.check([1])                   # single element
        self.check([1, 3, 5, 2, 4, 6])    # even length
        self.check([1, 3, 5, 2, 4, 6, 3]) # odd length, duplicate value
        for _ in range(100):              # random test cases
            self.check([randrange(100) for _ in range(randrange(100))])


if __name__ == "__main__":
     main()