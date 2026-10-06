class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        N = len(nums)
        dp = [None] * N
        dp[N - 1] = 1
        for i in range(N - 2, -1, -1):
            longest_sub = 1
            for j in range(i, N):
                if nums[i] < nums[j]:
                    longest_sub = max(longest_sub, dp[j] + 1)
            dp[i] = longest_sub
        return max(dp)
    

s = Solution()
print(s.lengthOfLIS([9,1,4,2,3,3,7]))
print(s.lengthOfLIS([1,4, 5, 2, 3,4]))
print(s.lengthOfLIS([1]))