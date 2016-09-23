from heapq import heappop, heappush


def heapify(arr):
    for root in range(len(arr) // 2 - 1, -1, -1):
        rootVal = arr[root]
        child = 2 * root + 1
        while child < len(arr):
            if child + 1 < len(arr) and arr[child] > arr[child + 1]:
                child += 1
            if rootVal <= arr[child]:
                break
            arr[child], arr[(child - 1) // 2] = arr[(child - 1) // 2], arr[child]
            child = child * 2 + 1
    return arr


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


'''
TRIES
'''

def insert_key(k, v , trie):
    #insert key into trie and put value in key's bucket
    pass


def has_key(k, trie):
    pass


def retrieve_val(k, trie):
    pass


def start_with_prefix(prefix, trie):
    pass


def make_trie(*words):
    _end = '_end'
    root = dict()
    for word in words:
        current_dict = root
        for char in word:
            current_dict = current_dict.setdefault(char, {})
        current_dict[_end] = _end
    return root

print(make_trie('foo', 'bar', 'baz', 'barz'))


def in_trie(trie, word):
    current_dict = trie
    for char in word:
        if char in current_dict:
            current_dict = current_dict[char]
        else:
            return False
