# Problem: Jump Game; Jump Game II
# canJump: Decide whether the last index is reachable from index 0. jump: Return the minimum
# jumps to reach it, with -1 for unreachable inputs in this file's extension. Each nonnegative
# value is the maximum forward jump length.
#
# Expected input/output: nums=[2,3,1,1,4] -> canJump true, jump 2; nums=[3,2,1,0,4] -> canJump
# false, jump -1

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        N = len(nums)
        mx, i = 0, 0

        while i <= mx:
            jumps = nums[i]
            mx = max(mx, i + jumps)

            if mx >= N - 1:
                return True
            i += 1
        return False

    def jump(self, nums: list[int]) -> bool:
        # dp(i) min hops to get from i to end
        # dp(i) = min over dp(i+j) for jumpable "j"s + 1
        N = len(nums)
        memo = [float("inf")] * N
        memo[N - 1] = 0

        for i in range(N - 2, -1, -1):
            m_j = float("inf")
            for j in range(1, nums[i] + 1):
                if i + j >= N:
                    break
                m_j = min(m_j, memo[i + j])
            memo[i] = m_j + 1

        return memo[0] if memo[0] != float("inf") else -1


s = Solution()
print(s.jump([1, 2, 0, 1, 0]))
print(s.jump([1, 2, 0, 4, 0]))
print(s.jump([1, 2, 1, 0, 0]))


# Key insight:
# Reachability needs only the farthest reachable index. Minimum-jump DP takes 1 plus the
# smallest future jump count among reachable next positions; greedy BFS layers can reduce this
# to linear time.
