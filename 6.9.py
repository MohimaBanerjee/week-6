from collections import deque

def orangesRotting(mat):
    n = len(mat)
    m = len(mat[0]) if n > 0 else 0

    queue = deque()
    fresh_count = 0

    # Step 1: Initialize queue with all rotten oranges and count fresh oranges
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                queue.append((i, j))
            elif mat[i][j] == 1:
                fresh_count += 1

    # If no fresh oranges, return 0
    if fresh_count == 0:
        return 0

    time = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # Step 2: BFS to rot adjacent fresh oranges
    while queue and fresh_count > 0:
        time += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check boundaries and if fresh orange
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                    mat[nx][ny] = 2  # Rot the orange
                    fresh_count -= 1
                    queue.append((nx, ny))

    # If fresh oranges remain, return -1
    return time if fresh_count == 0 else -1

# Example usage:
mat1 = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
print(orangesRotting(mat1))  # Output: 1

mat2 = [[2, 2, 0, 1]]
print(orangesRotting(mat2))  # Output: -1

mat3 = [[2, 2, 2], [0, 2, 0]]
print(orangesRotting(mat3))  # Output: 0
