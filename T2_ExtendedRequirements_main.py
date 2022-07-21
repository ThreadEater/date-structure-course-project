from Stack import Stack
import BTreeVisualization as BTV
from BTree import BTree
       
prec = {'*': 2,'/': 2, '+': 1,'-':1,'(': 0, ')': 0}

def infix_to_postfix(expr):
    ops = Stack()
    postfix = []
    toks = expr.split()

    for c in toks:
        if c == '(':
            ops.push(c)
        elif c == ')':
            while ops.peek() != '(':
                postfix.append(ops.pop())
            ops.pop()
        elif c.isdigit():
            postfix.append(c)
        else:
            while bool(ops) and prec[ops.peek()] >= prec[c]:
                postfix.append(ops.pop())
            ops.push(c) 
    while bool(ops):
        postfix.append(ops.pop())
    return postfix

def turnTree(postfix):
    s=Stack()
    for i in postfix:
        if i.isdigit():
            s.push(BTree.Node(i))
        elif i in ['+','-','/','*']:
            a=s.pop()
            b=s.pop()
            tmp=BTree.Node(i,left=b,right=a)
            BTree.pprint(tmp)
            s.push(tmp)
    
    t=BTree()
    t.root=s.pop()
    return t

def calculate(node):
    if node:
        if node.val not in ('+','-','*','/'):
            return int(node.val)
        elif node.val =='+':
            return calculate(node.left) + calculate(node.right)
        elif node.val == '-':
            return calculate(node.left) - calculate(node.right)
        elif node.val == '*':
            return calculate(node.left) * calculate(node.right)
        elif node.val == '/':
            return calculate(node.left) / calculate(node.right)

a=input()
a=infix_to_postfix(a)
print(a)
a=turnTree(a)
print(calculate(a.root))

