from collections import deque

def firstNonRepeating(s):
    freq = {}
    q = deque()
    result = []

    for ch in s:
        # Update frequency
        freq[ch] = freq.get(ch, 0) + 1

        # Add current character to queue
        q.append(ch)

        # Remove characters from front of queue if they are repeating
        while q and freq[q[0]] > 1:
            q.popleft()

        # Append the first non-repeating character or '#' if none
        if q:
            result.append(q[0])
        else:
            result.append('#')

    return "".join(result)

# Example usage:
print(firstNonRepeating("aabc"))  # Output: "a#bb"
print(firstNonRepeating("zz"))    # Output: "z#"
print(firstNonRepeating("bb"))    # Output: "b#"