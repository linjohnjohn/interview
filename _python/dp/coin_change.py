class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp(i, x) = given coins starting from index i can we make $x

        memo = {}

        def dp(i, x):
            if x == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i, x) in memo:
                return memo[(i, x)]
            
            coin = coins[i]
            max_curr_coin = x // coin
            possibilities = 0

            for tokens in range(max_curr_coin, -1, -1):
                possibilities += dp(i + 1, x - tokens * coin)
            
            memo[(i, x)] = possibilities
            return possibilities

        
        return dp(0, amount)


s = Solution()
print(s.change(4, [1,2,3]))
print(s.change(7, [2, 4]))
print(s.change(7, [1, 5, 10]))