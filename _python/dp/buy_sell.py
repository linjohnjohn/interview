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