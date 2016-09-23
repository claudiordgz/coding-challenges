from collections import defaultdict
from fixture import get_testcase,read_raw

class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """
    def __init__(self):
        self.root = defaultdict()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
            if "_count" not in current:
                current["_count"] = 1
            else:
                current["_count"] += 1
        current.setdefault("_end")

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return 0
            current = current[letter]
        if "_end" in current:
            return current["_count"]
        return current["_count"]

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True


def test_1():
    tr = Trie()
    tr.insert('hack')
    tr.insert('hackerrank')

    print(tr.search('hac'))
    print(tr.search('hak'))


def test_2():
    tr = Trie()
    tr.insert('s')
    tr.insert('ss')
    tr.insert('sss')
    tr.insert('ssss')
    tr.insert('sssss')

    print(tr.search('s'))
    print(tr.search('ss'))
    print(tr.search('sss'))
    print(tr.search('ssss'))
    print(tr.search('sssss'))
    print(tr.search('ssssss'))


def solution(data):
    tr = Trie()
    #data = [l for l in fileinput.input()]
    n = int(data[0])
    words = data[1:]
    for letters in words:
        stuff = [l for l in letters.split()]
        cmd, i = stuff[0], stuff[1]
        if cmd == 'add':
            tr.insert(i)
        elif cmd == 'find':
            yield tr.search(i)


if __name__ == '__main__':
    for t in '01':
        i, o = get_testcase(t, read_as=read_raw)
        o = list(map(int, o))
        for gen, out in zip(solution(i), o):
            print(gen == out)
