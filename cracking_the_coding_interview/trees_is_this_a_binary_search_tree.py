'''

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen
'''

import sys


def check_bst(root, m_min, m_max):
    if not root:
        return True

    return (m_min < root.data < m_max and
            check_bst(root.left, m_min, root.data) and
            check_bst(root.right, root.data, m_max)
            )


def check_binary_search_tree_(root):
    return check_bst(root, -sys.maxsize, sys.maxsize)


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


l_1 = node(1)
l_4 = node(4)
l_5 = node(5)
l_5.left = l_1
l_5.right = l_4

r_3 = node(3)
r_3.left = l_5

r_2 = node(2)

r_3.right = r_2

r_6 = node(6)
r_2.left = r_6

print(check_binary_search_tree_(r_3))