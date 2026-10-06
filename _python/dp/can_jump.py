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
