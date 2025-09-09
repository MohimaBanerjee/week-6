class Queue:
    def __init__(self):
        self.queue = []
        self.front_index = 0  # To optimize pop operation

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.front_index == len(self.queue):
            return -1
        popped_element = self.queue[self.front_index]
        self.front_index += 1
        # Optional: clear memory if front_index grows large
        if self.front_index > 1000:
            self.queue = self.queue[self.front_index:]
            self.front_index = 0
        return popped_element


# Example usage:
if __name__ == "__main__":
    q = Queue()
    queries = [1, 2, 1, 3, 2, 1, 4, 2]
    for i in range(len(queries)):
        if queries[i] == 1:
            q.push(queries[i+1])
            i += 1
        elif queries[i] == 2:
            print(q.pop(), end=" ")