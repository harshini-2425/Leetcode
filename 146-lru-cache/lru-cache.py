class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode    
    def add(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value
 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
        if len(self.cache) >= self.capacity:
            node = self.tail.prev
            self.remove(node)
            del self.cache[node.key]
        newnode = Node(key,value)
        self.add(newnode)
        self.cache[key] = newnode



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)