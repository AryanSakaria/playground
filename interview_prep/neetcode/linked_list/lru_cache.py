class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0,0), Node(0,0)   
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        tail_node = self.tail.prev
        tail_node.next = node
        node.prev = tail_node
        node.next = self.tail
        self.tail.prev = node


    def remove(self, prev, node):
        prev.next = node.next
        node.next.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key].prev, self.cache[key])
            self.insert(self.cache[key])
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key].prev, self.cache[key])
            self.insert(self.cache[key])
        else:
            new_val = Node(key, value)
            self.insert(new_val)
            self.cache[key] = new_val
        if len(self.cache) > self.capacity:
            head_next = self.head.next
            self.head.next = head_next.next
            self.head.next.prev = self.head
            del self.cache[head_next.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)