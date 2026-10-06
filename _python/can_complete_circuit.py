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
