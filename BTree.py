import networkx as nx
import matplotlib.pyplot as plt


class BTree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    def __iter__(self):
        def iter_rec(n):
            if n:
                yield from iter_rec(n.left)
                yield from iter_rec(n.right)
                yield n
        return iter_rec(self.root)
        
    
    def __init__(self):
        self.root = None

    def height(node):
       def height_rec(t):
           if not t:
               return 0
           else:
               return 1 + max(height_rec(t.left), height_rec(t.right))
       return height_rec(node)

    def pprint(node,width=128):
        height = BTree.height(node)
        nodes  = [(node, 0)]
        prev_level = 0
        repr_str = ''
        while nodes:
            n,level = nodes.pop(0)
            if prev_level != level:
                prev_level = level
                repr_str += '\n'
            if not n:
                if level < height-1:
                    nodes.extend([(None, level+1), (None, level+1)])
                repr_str += '{val:^{width}}'.format(val='-', width=width//2**level)
            elif n:
                if n.left or level < height-1:
                    nodes.append((n.left, level+1))
                if n.right or level < height-1:
                    nodes.append((n.right, level+1))
                repr_str += '{val:^{width}}'.format(val=n.val, width=width//2**level)
        print(repr_str)
        print('-'*128)
        
    

    
    


