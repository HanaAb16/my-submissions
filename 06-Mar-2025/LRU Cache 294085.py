# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, val = 0 , key = 0 , next = None , prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

    def __str__(self):
        return f'{self.val} - {self.key}'

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.dummy = Node()
        self.tail = self.dummy
        self.capacity = capacity
        self.count = 0

    def update(self, node):
        if node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = self.tail.next
    def get(self, key: int) -> int:
        if key in self.d: 
            self.update(self.d[key])
            return self.d[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
                self.d[key].val = value
                self.update(self.d[key])
                return

        new = Node(value , key)
        if self.count < self.capacity:
            self.count += 1
        else:
            del self.d[self.dummy.next.key]
            if self.tail == self.dummy.next:
                self.tail = self.dummy

            if self.dummy.next:
                print(self.dummy.next.next)
                self.dummy.next = self.dummy.next.next
                if self.dummy.next:
                    self.dummy.next.prev = self.dummy
 
        self.d[key] = new
        self.tail.next = new
        new.prev = self.tail
        self.tail = self.tail.next
        print(self.dummy.next , self.tail)
            

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)