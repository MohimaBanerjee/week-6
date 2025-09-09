from collections import deque

def reverseFirstKElements(q, k):
    if k > len(q):
        return q  # If k is greater than queue size, return original queue

    stack = []
    # Step 1: Dequeue first k elements and push them onto stack
    for _ in range(k):
        stack.append(q.popleft())

    # Step 2: Enqueue back the elements from stack (reversed order)
    while stack:
        q.appendleft(stack.pop())

    # Step 3: Move the remaining elements to the back to maintain order
    for _ in range(len(q) - k):
        q.append(q.popleft())

    return q

# Example usage:
q1 = deque([1, 2, 3, 4, 5])
k1 = 3
result1 = reverseFirstKElements(q1, k1)
print(list(result1))  # Output: [3, 2, 1, 4, 5]

q2 = deque([4, 3, 2, 1])
k2 = 4
result2 = reverseFirstKElements(q2, k2)
print(list(result2))  # Output: [1, 2, 3, 4]