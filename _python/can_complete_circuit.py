# Problem: Gas Station
# Given fuel at each circular station and fuel cost to the next station, return a starting
# index that completes the circuit from an empty tank, or -1.
#
# Expected input/output: gas=[1,2,3,4,5], cost=[3,4,5,1,2] -> 3; gas=[2,3,4], cost=[3,4,3] ->
# -1

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        N = len(gas)
        net = [gas[i] - cost[i] for i in range(N)]

        fuel = 0
        candidate = 0
        debt = 0
        for i in range(N):
            new_fuel = fuel + net[i]
            if new_fuel >= 0:
                fuel = new_fuel
            else:
                candidate = i + 1
                fuel = 0
                debt += new_fuel

        if fuel + debt >= 0:
            return candidate
        else:
            return -1


s = Solution()
print(s.canCompleteCircuit([1, 0, -2, 1], [0, 0, 0, 0]))
print(s.canCompleteCircuit([1, 0, -2, 1, 0, -2], [0, 0, 0, 0, 0, 0]))

gas = [3, 1, 1]
cost = [1, 2, 2]
print(s.canCompleteCircuit(gas, cost))


# Key insight:
# When a running fuel balance becomes negative, skip all starts in that segment. A candidate
# works exactly when the total balance is nonnegative.
