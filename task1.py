class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.payload
        
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findMin(self):
        while self.hasLeftChild():
             self = current.leftChild
        return self
            
            
            
class BinarySearchTree:

    def __init__(self,alist=None):
        if not alist:
            self.root = None
            self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size
    
    def buildTreeWithNode(self, treeNode):
        self.put(treeNode.getKey(),treeNode.getValue())
    
    def buildTreeWithList(self, keylist):
        if not keylist:
            print "no action for vacant list"
        else:
            for item in keylist:
                 #initialize all the node rank to be 0
                 self.put(item,0)
                    
    def initRank(self):
        self.root.payload = 0
        self.preorderInit(self.root)

    
    def preorderInit(self,currentNode):
        
        if currentNode.isLeftChild():
            currentNode.payload = currentNode.parent.payload-1
        elif currentNode.isRightChild():
            currentNode.payload = currentNode.parent.payload+1
        elif currentNode.hasLeftChild():
            self.preorderInit(currentNode.leftChild)
        elif currentNode.hasRightChild():
            self.preorderInit(currentNode.rightChild)
        else:
            return
       
    
            
    def printTree(self,printValue=False):
        #print Tree with inorder
        if self.root:
            self.inorderPrint(self.root,True)
        else:
            if  printValue:
                print ("Key:%s , Rank:%s" % (self.root.getKey(),self.root.getValue()))
            else:
                print self.root.getKey()
            
    def inorderIterNode(self,key):
        currentNode = self._get(key,self.root)
        if currentNode.isRoot():
           self.printTree()
        else:
           self.inorderPrint(currentNode)
    
    def inorderPrint(self,currentNode,printValue=False):
        if currentNode.hasLeftChild():
            self.inorderPrint(currentNode.leftChild,True)
        if printValue:
            print ("Key:%s , Rank:%s" % (currentNode.getKey(),currentNode.getValue()))
        else:
            print currentNode.getKey()
        if currentNode.hasRightChild():
            self.inorderPrint(currentNode.rightChild,True)
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False
      
    def findSuccessor(self,key):
          currentNode = self._get(key,self.root)
          succ = None
          if currentNode.hasRightChild():
              succ = currentNode.rightChild.findMin()
         
          else:
    
              if currentNode.parent:
                   if currentNode.isLeftChild():
                       succ = currentNode.parent
                   else:
                       currentNode.parent.rightChild = None
                       succ = self.findSuccessor(currentNode.parent.key)
                       currentNode.parent.rightChild = self
      
          return succ
    

mytree = BinarySearchTree()
mytree.buildTreeWithList([7,2,3,5,8,9,10,6,4])
#mytree.printTree()
mytree.initRank()
mytree.printTree(True)

#mytree = BinarySearchTree()
#mytree.put(4,'blue')
#mytree.put(3,'red')
#mytree.put(1,'pink')
#mytree.put(2,'grey')
#mytree.put(7,'blue')
#mytree.put(4,'rank')
#mytree.put(5,'yellow')
#print (mytree.findSuccessor(4).getKey())
#mytree.traverseNodeInOrder(4)
#mytree.printTree()
#mytree[3]="red"
#mytree[4]="blue"
#mytree[6]="yellow"
#mytree[2]="at"
#mynode1 = TreeNode(3,'red')
#mynode2 = TreeNode(4,'blue')
#mynode3 = TreeNode(2,'grey')
#print(mytree[6])
#print(mytree[2])
#print(mytree.findSuccessor(2))
#mytree.buildTree(mynode1)
#mytree.buildTree(mynode2)
#mytree.buildTree(mynode3)
#mytree.printTree()