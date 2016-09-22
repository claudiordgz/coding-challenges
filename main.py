
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(root):
    if root is None:
        return
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data)
    in_order(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)


def main():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    a.left = b
    a.right = c
    pre_order(a)
    in_order(a)
    post_order(a)
    print("just chilling")
    a = [x for x in range(5, 2000)]
    print(a)

if __name__ == '__main__':
    main()