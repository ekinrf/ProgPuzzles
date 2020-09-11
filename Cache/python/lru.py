class BiDNode:
    def __init__(self, key, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = {}
        # create fake head and end to make implementation easier
        self.lru_queue_head = BiDNode(-1, -1)
        self.lru_queue_end = BiDNode(-1, -1)
        self.lru_queue_head.next, self.lru_queue_end.prev = self.lru_queue_end, self.lru_queue_head

    def get(self, key):
        if key in self.values:
            lru_queue_node = self.values[key]
            self.remove_from_queue(lru_queue_node)
            self.add_to_queue_head(lru_queue_node)
            return self.values[key].val
        return -1

    def put(self, key, value):
        if key in self.values:
            self.remove_from_queue(self.values[key])
            del self.values[key]

        if len(self.values) == self.capacity:
            least_used_key = self.lru_queue_end.prev.key
            del self.values[least_used_key]
            self.remove_from_queue(self.lru_queue_end.prev)

        node = BiDNode(key, value)
        self.values[key] = node
        self.add_to_queue_head(node)

    def remove_from_queue(self, lru_queue_node):
        # because of fake head and end, we are sure prev and next always exist
        lru_queue_node.prev.next, lru_queue_node.next.prev = lru_queue_node.next, lru_queue_node.prev

    def add_to_queue_head(self, node):
        self.lru_queue_head.next.prev = node
        node.prev = self.lru_queue_head
        node.next = self.lru_queue_head.next
        self.lru_queue_head.next = node


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))