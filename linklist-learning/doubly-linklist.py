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

    # def insertAnyLocation(self,value,valueLocation):
    #     temp = Node(value)
    #     if self.head == None:
    #         self.head = temp
    #         return True

    #     t = self.head
    #     while t.next != None:
    #         if t.data == value:
    #             break
    #         else:
    #             t = t.next

    #         temp.next = t.next
    #         t.next.pre
        

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
obj.insertAtStart(40)
# obj.insertAnyLocation(35,30)
obj.printMyList()