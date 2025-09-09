from collections import deque

def interleaveQueue(q):
    n = len(q)
    if n % 2 != 0:
        # If queue size is not even, return as is (or handle as needed)
        return q

    half = n // 2
    first_half = deque()
    
    # Step 1: Dequeue first half elements and store in first_half
    for _ in range(half):
        first_half.append(q.popleft())
    
    # Step 2: Interleave elements from first_half and remaining queue
    while first_half:
        q.append(first_half.popleft())  # from first half
        q.append(q.popleft())            # from second half

    return q

# Example usage:
q1 = deque([2, 4, 3, 1])
result1 = interleaveQueue(q1)
print(list(result1))  # Output: [2, 3, 4, 1]

q2 = deque([3, 5])
result2 = interleaveQueue(q2)
print(list(result2))  # Output: [3, 5]