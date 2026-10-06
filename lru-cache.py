class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self,node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insertNodeAtEnd(self,node):
        prev, next = self.tail.prev, self.tail
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertNodeAtEnd(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key:int, value:int):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insertNodeAtEnd(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.head.next
            self.remove(LRU)
            del self.cache[LRU.key]


obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
