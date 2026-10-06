VALID_INT = set()
for i in range(1, 27):
    VALID_INT.add(str(i))

class Solution:
    
    def numDecodings(self, s: str) -> int:
        # dp(i) = decode(1 char) if valid + dp(i + 1) + decode(2 char) if valid + dp(i + 2)
        N = len(s)
        dp = [0] * N
        dp.append(1)
        dp.append(1)

        for i in range(N - 1, -1, -1):
            if s[i] in VALID_INT:
                dp[i] += dp[i + 1]

            if i + 1 < N and s[i:i+2] in VALID_INT:
                dp[i] += dp[i + 2]
        
        return dp[0]
    

s = Solution()

print(s.numDecodings("01"))
print(s.numDecodings("111"))


