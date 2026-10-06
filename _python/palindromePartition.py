import math

class Solution:
    def isPalindrome(self, s):
        N = len(s)
        for x in range(0, math.ceil(N / 2)):
            if s[x] != s[N - x - 1]:
                return False
        return True

    def partition(self, s: str) -> list[list[str]]:
        memo = [None] * len(s)

        def dp(i):
            if i == len(s):
                return [[]]
            
            if memo[i]:
                return memo[i]
            ans = []
            for x in range(i + 1, len(s) + 1):
                candidate = s[i: x]
                if self.isPalindrome(candidate):
                    otherPalindromes = dp(x)
                    for ps in otherPalindromes:
                        newPs = ps.copy()
                        newPs.append(candidate)
                        ans.append(newPs)
            
            memo[i] = ans
            return ans
        
        return dp(0)
    

s = Solution()
print(s.partition('aab'))
print(s.partition('aabba'))