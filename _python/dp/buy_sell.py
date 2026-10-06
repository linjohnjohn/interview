# Problem: Best Time to Buy and Sell Stock with Cooldown
# Find the maximum stock profit with unlimited transactions, holding at most one share. After
# selling, wait one full day before buying again.
#
# Expected input/output: prices=[1,2,3,0,2] -> 3; prices=[1] -> 0

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # dp(i) max profit starting at day i
        # dp(i) = p[j] - p[i] + dp(j+2) for j in (i, N] or dp(i + 1)
        N = len(prices)
        dp = [0] * (N + 2)

        for i in range(N - 2, -1, -1):
            gain = dp[i + 1]
            for j in range(i + 1, N, 1):
                gain = max(gain, prices[j] - prices[i] + dp[j + 2])
            
            dp[i] = gain

        return dp[0]
    

s = Solution()
print(s.maxProfit([1,3,4,0,4]))
print(s.maxProfit([1,3]))
print(s.maxProfit([3]))
print(s.maxProfit([]))

# Key insight:
# If buying on day i and selling on day j, the next buying opportunity is j+2. Compare this
# with skipping day i and memoize future profit.
