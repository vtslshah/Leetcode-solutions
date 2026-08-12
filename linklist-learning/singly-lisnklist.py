class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class singlyLinkList:
    def __init__(self, head= None):
        self.head = head

    def insertAtEnd(self,value):
        temp = Node(value)
        if self.head != None:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtStart(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMiddle(self,value,nodeValue):
        temp = Node(value)
        t1 = self.head
        while t1.next != None:
            if t1.data == nodeValue:
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteNode(self,value):
        t1 = self.head
        prev = t1
        if t1.data == value:
            self.head = t1.next
            return True
    
        while t1.next != None:
            if t1.data == value:
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if t1.data == value:
            prev.next = None  

    def printMyList(self):
        myList = self.head
        while myList.next != None:
            print(myList.data)
            myList = myList.next
        print(myList.data)
        # print(type(myList))
        
obj = singlyLinkList()
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(50)
obj.insertAtStart(10)
obj.insertAtMiddle(40,30)
obj.deleteNode(50)
obj.printMyList()