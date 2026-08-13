class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkList:
    def __init__(self, head= None):
        self.head = head

    def InsetToEnd(self,value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return True
        
        t = self.head
        while t.next != None:
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtStart(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAnyLocation(self,value,valueLocation):
        t = self.head
        while t.next != None:
            if t.data == valueLocation:
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def deleteNode(self,value):
        t = self.head
        if t.data == value:
            self.head = t.next
            t.next.prev = None
            return True
        while t.next != None:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return True
            else:
                t = t.next
        if t.data == value:
            t.prev.next = None

    def printMyList(self):
        t = self.head
        while t.next != None:
            print(t.data)
            t = t.next
        print(t.data)

obj = DoublyLinkList()
obj.InsetToEnd(10)
obj.InsetToEnd(20)
obj.InsetToEnd(30)
obj.insertAtStart(1)
obj.insertAnyLocation(25,20)
obj.deleteNode(30)
obj.printMyList()