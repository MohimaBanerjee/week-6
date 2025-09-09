class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail nodes to avoid empty states
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node):
        """Add node right before tail (most recently used)."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Move the accessed node to the tail (most recently used)
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Update the value and move node to tail
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove least recently used node (head.next)
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)

# Example usage:
if __name__ == "__main__":
    cap = 2
    queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5], ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4], ["PUT", 1, 2], ["GET", 3]]
    lru_cache = LRUCache(cap)
    output = []
    for query in queries:
        if query[0] == "PUT":
            lru_cache.put(query[1], query[2])
        elif query[0] == "GET":
            output.append(lru_cache.get(query[1]))
    print(output)  # Output: [5, -1]