# Problem: Partition Equal Subset Sum
# Decide whether positive integers can be divided into two subsets with equal sums, using
# every element exactly once.
#
# Expected input/output: nums=[1,5,11,5] -> true; nums=[1,2,3,5] -> false

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # dp(i, sum) given subarray nums[i:], can we make sum?
        # OR over dp(i + 1, sum - n_i) dp(i + 1, sum)
        # dp(i, 0) = true

        sum = 0
        for n in nums:
            sum += n
        if sum % 2 == 1:
            return False
        target = sum / 2

        return self.make_sum(nums, target)

    def make_sum(self, nums: list[int], target: int):
        N = len(nums)
        memo = {}

        def dp(i, targ):
            if targ == 0:
                return True
            if i >= N:
                return False

            if (i, targ) not in memo:
                memo[(i, targ)] = dp(i + 1, targ - nums[i]) or dp(i + 1, targ)
            
            return memo[(i, targ)]
        
        return dp(0, target)
                

s = Solution()
print(s.canPartition([1,2,3,4]))
print(s.canPartition([1,2,3,4, 5]))
print(s.canPartition([1,5,11,5]))


# Key insight:
# An odd total is impossible. Otherwise find a subset summing to half the total, memoizing
# include/skip decisions by index and remaining sum.
