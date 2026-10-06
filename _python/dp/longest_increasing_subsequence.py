# Problem: Longest Increasing Subsequence
# Return the longest strictly increasing subsequence length. Chosen elements keep their
# original order but need not be adjacent.
#
# Expected input/output: nums=[10,9,2,5,3,7,101,18] -> 4; nums=[7,7,7] -> 1

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

# Key insight:
# DP at index i is 1 plus the best subsequence starting at a later, larger value; equal values
# cannot extend it.
