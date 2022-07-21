from Stack import Stack
import BTreeVisualization as BTV
from BTree import BTree

def isalpha(word):
    for i in ('!','∧','∨','(',')',' '):
        if i in word:
            return False
    return True
    
def findArgument(expr):
    arguments=[]
    temp=expr.split()
    for i in temp:
        if i not in  ('!','∧','∨','(',')',' '):
            arguments.append(i)
    return arguments
            
def check(expr):
    s = Stack()
    expr=expr
    if expr[0] in ['∧','∨']:
        return False
    elif (expr[-1] in ['∧','∨','!']):
        return False
    else:
        for i in range(len(expr)):
            if i<len(expr)-1:
                if expr[i] in ['∧','∨']:
                    if expr[i+1] in ['∧','∨',')']:
                        return False
                elif expr[i]=='!':
                    if expr[i+1] in ['∧','∨',')']:
                        return False
                elif expr[i]=='(':
                    if expr[i+1] in ['∧','∨']:
                        return False
                elif expr[i]==')':
                    if expr[i+1]=='!':
                        return False
                    
            if expr[i] == '(':
                s.push(expr[i])
            elif expr[i] == ')':
                if s.empty():
                    return False
                elif s.pop() != '(':
                    return False
                
    return s.empty()
                
prec = {'!': 2,'∧': 1, '∨': 1,'(': 0, ')': 0}

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
        elif isalpha(c):
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
        if isalpha(i):
            s.push(BTree.Node(i))
        elif i=='!':
            a=s.pop()
            tmp=BTree.Node(i,left=None,right=a)
            BTree.pprint(tmp)
            BTV.draw(tmp)
            s.push(tmp)
        elif i in ['∧','∨']:
            a=s.pop()
            b=s.pop()
            tmp=BTree.Node(i,left=b,right=a)
            BTree.pprint(tmp)
            BTV.draw(tmp)
            s.push(tmp)
    
    t=BTree()
    t.root=s.pop()
    return t

def calculate(node):
    if node:
        if node.val not in ('∧','∨','!'):
            return values[node.val]
        elif node.val =='!':
            return not calculate(node.left)
        elif node.val == '∧':
            return calculate(node.left) and calculate(node.right)
        elif node.val == '∨':
            return calculate(node.left) or calculate(node.right)

def enum(arguements):
    lst=[]
    for i in range(2**len(arguments)):
        dic={}
        s=str(bin(i))[2::]
        if len(s)<len(arguments):
            s='0'*(len(arguments)-len(s))+s
        s=[int (k) for k in s]
        for j in range(len(arguments)):
            dic[arguments[j]]=s[j]
        lst.append(dic)
    return lst

print("请输入命题公式 示例:( ! A ∧ B ) ∨ C")
expr=input()
values=None
legal=check(expr)
while not legal:
    print("Retry!")
    expr=input()
    legal=check(expr)
else:
    arguments=findArgument(expr)
    expr1=infix_to_postfix(expr)
    print(' '.join(expr1))
    t=turnTree(expr1)
    explain=enum(arguments)
    BTree.pprint(t.root)
    
    for i in range(2**len(arguments)):
        values=explain[i]
        print(explain[i],calculate(t.root))
