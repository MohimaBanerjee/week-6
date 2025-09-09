class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, x):
        new_node = Node(x)
        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def pop(self):
        if self.front is None:
            return -1
        popped_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            # If queue becomes empty, update rear as well
            self.rear = None
        return popped_data

# Example usage:
if __name__ == "__main__":
    Q = 5
    queries = [[1, 2], [1, 3], [2], [1, 4], [2]]
    q = Queue()
    for query in queries:
        if query[0] == 1:
            q.push(query[1])
        elif query[0] == 2:
            print(q.pop(), end=" ")