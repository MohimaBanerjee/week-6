class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            # Transfer all elements from s1 to s2 if s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return -1
        return self.s2.pop()

# Example usage:
if __name__ == "__main__":
    q = QueueUsingStacks()
    queries = [[1, 2], [1, 3], [2], [1, 4], [2]]
    output = []
    for query in queries:
        if query[0] == 1:
            q.push(query[1])
        elif query[0] == 2:
            output.append(q.pop())
    print(output)  # Output: [2, 3]

    # Another example
    q2 = QueueUsingStacks()
    queries2 = [[1, 2], [2], [2], [1, 4]]
    output2 = []
    for query in queries2:
        if query[0] == 1:
            q2.push(query[1])
        elif query[0] == 2:
            output2.append(q2.pop())
    print(output2)  # Output: [2, -1]