class node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        """ Insert new node from data
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    


def get_ancestor(root, node1, node2):
    if not root:
        return
    
    if root.data < node1 and root.data < node2:
        return  get_ancestor(root.right, node1, node2)
    elif root.data > node1 and root.data > node2:
        return get_ancestor(root.left, node1, node2)
    else:
        return root


def bstDistance(values, n, node1, node2): 
    root = node(values[0])
    for n in values[1:]:
        root.insert(n)
    
    common_root = get_ancestor(root, node1, node2)
    
    if not common_root:
        return
    
    left = common_root
    right = common_root
    
    l, r = 0, 0
    while left:
        if left.data > node1:
            left = left.left
            l += 1 
        elif left.data < node1:
            left = left.right
            l += 1 
        else:
            break
        
    while right:
        if right.data > node2:
            right = right.left
            r += 1 
        elif right.data < node2:
            right = right.right
            r += 1 
        else:
            break
        
    return l+r 



if __name__ == '__main__':
    bstDistance([9,7,5,3,1], 5, 7, 20)