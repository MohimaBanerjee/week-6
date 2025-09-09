def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    start = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start

# Example usage:
gas = [4, 5, 7, 4]
cost = [6, 6, 3, 5]
print(canCompleteCircuit(gas, cost))  # Output: 2

gas = [3, 9]
cost = [7, 6]
print(canCompleteCircuit(gas, cost))  # Output: -1