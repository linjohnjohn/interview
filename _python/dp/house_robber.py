# Problem: House Robber
# Houses lie in a straight row. Return the maximum money you can steal without robbing
# adjacent houses. rob and rob2 here solve the same linear problem.
#
# Expected input/output: nums=[1,2,3,1] -> 4; nums=[2,7,9,3,1] -> 12

class Solution:
    def rob2(self, nums: list[int]) -> int:
        # dp(i) = max gain at house i
        # dp(i) = max: dp(i+1), nums[i] + dp(i+2)
        N = len(nums)
        if N == 1:
            return nums[0]
        dp = [0] * N
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])
        for i in range(N - 3, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        
        return dp[0]

    def rob(self, nums: list[int]) -> int:
        # dp(i) = max gain at house i
        # dp(i) = max: dp(i+1), nums[i] + dp(i+2)
        N = len(nums)
        if N == 1:
            return nums[0]
        nums[-2] = max(nums[-1], nums[-2])
        for i in range(N - 3, -1, -1):
            nums[i] = max(nums[i + 1], nums[i] + nums[i + 2])
        
        return nums[0]

s = Solution()
print(s.rob([1, 1, 3, 3]))
print(s.rob([1, 3]))

# Key insight:
# At each house, choose between skipping it and taking its money plus the best result starting
# two houses later.
