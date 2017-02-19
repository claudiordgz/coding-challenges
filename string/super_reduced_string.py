

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None



def main(s):   
    root = Node(s[0])
    itr = root
    for ch in s[1:]:
        if itr is None:
            if root is itr:
                root = Node(ch)
                itr = root
            else:
                itr = Node(ch)
        elif itr.data != ch:
            itr.right = Node(ch)
            itr.right.left = itr
            itr = itr.right
        else:
            if root is itr:
                root = None
                itr = root
            else:
                itr = itr.left
                itr.right = None

    itr = root
    ret_string = []
    while itr:
        ret_string.append(itr.data)
        itr = itr.right
    return ''.join(ret_string) if ret_string else 'Empty String'


def main_two(string):
    # i: to iterate over the string, starting at 1.
    i = 1
    # While the iterator hasn't exceeded the remaining.
    while i < len(string):
        cur, pre = string[i], string[i-1]
        # Compare characters that are together.
        if cur == pre:
            # If they are equal, remove them from the string
            string = string[:i-1] + string[i+1:]
            # After removal, set back the iterator by two,
            # or if it gets negative, put it at the start.
            i = max(i-2, 0)
        # Advance the iterator.
        i += 1
    if string == "":
        return "Empty String"
    else:
        return string
    


import time

def st_time(func):
    """
        st decorator to calculate the total time of a func
    """

    def st_func(*args, **keyArgs):
        t1 = time.time()
        r = func(*args, **keyArgs)
        t2 = time.time()
        print("Function=%s, Time=%s" % (func.__name__, t2 - t1))
        return r

    return st_func


@st_time
def test():
    main('aaabccddd')
    main('aa')
    main('baab') 
    main('abba')
    main('lrfkqyuqfjjfquyqkfrlkxyqvnrtyssytrnvqyxkfrzrmzlygffgylzmrzrfveulqfpdbhhbdpfqluevlqdqrrcrwddwrcrrqdql')

@st_time
def test_two():
    main_two('aaabccddd')
    main_two('aa')
    main_two('baab') 
    main_two('abba')
    main_two('lrfkqyuqfjjfquyqkfrlkxyqvnrtyssytrnvqyxkfrzrmzlygffgylzmrzrfveulqfpdbhhbdpfqluevlqdqrrcrwddwrcrrqdql')


if __name__ == '__main__':
    test()
    test_two()