class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous == None:
            #first node is to be removed
                self.head = current.getNext()
            elif current.getNext == None:
            #last node is to be removed
                previous.next = None
            else:
            #node in the middile is to be removed
                previous.setNext(current.getNext())
        else:
            print ("Error, item not in the list!!")
    
    def append(self,item):
        temp = Node(item)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(temp)
    
    def show(self):
        j = 0
        current = self.head
        while current != None:
            print ("Node%d:"%j)
            print current.getData()
            current = current.getNext()
            j = j+1


mylist = UnorderedList()
mylist.add(31)
mylist.add(35)
mylist.add(37)
mylist.add(38)
mylist.add(39)
mylist.add(40)
mylist.show()