class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    
     def show(self):
         print self.items
         

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    def getRightChildVal(self):
        return self.rightChild.key
    
    def getLeftChildVal(self):
        return self.leftChild.key


#r = BinaryTree('a')
#print(r.getRootVal())
#r.setRootVal('aVal')
#print(r.getRootVal())
#r.insertLeft('b')
#print(r.getLeftChild().getRootVal())
#r.insertRight('c')
#print(r.getRightChild().getRootVal())
#r.getRightChild().setRootVal('hello')
#print(r.getRightChild().getRootVal())
def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#pt = buildParseTree(" 3 + 5 ")
#pt.postorder()  #defined and explained in the next section
import operator
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    print leftC.getRootVal()
    rightC = parseTree.getRightChild()
    print rightC.getRootVal()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        print fn
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
print evaluate(pt)
