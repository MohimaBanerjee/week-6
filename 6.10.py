class QueueUsingStacks:
    def __init__(self):
        self.s1 = []  # stack for enqueue
        self.s2 = []  # stack for dequeue

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            # Move all elements from s1 to s2 if s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()
        return None  # Should not happen as per problem constraints

    def front(self):
        if not self.s2:
            # Move all elements from s1 to s2 if s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2[-1]
        return None  # Should not happen as per problem constraints

if __name__ == "__main__":
    q = QueueUsingStacks()
    n = int(input())
    for _ in range(n):
        query = input().strip().split()
        if query[0] == '1':
            # Enqueue
            q.enqueue(int(query[1]))
        elif query[0] == '2':
            # Dequeue
            q.dequeue()
        elif query[0] == '3':
            # Print front
            print(q.front())
