class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp(j) = Given string s', how many distinct subsequence of s' are equal to t[j:]
        # new_dp(j) = Given string s = c + s' ...
        #   if c and t[j] match, then += dp(j + 1)
        #   += dp(j) b/c s can always have dp(j) distinct subsequences of t[j:]

        S, T = len(s), len(t)
        memo = [0] * T
        memo.append(1)

        for i in range(S - 1, -1, -1):
            new_memo = [0] * T
            new_memo.append(1)
            for j in range(T - 1, -1, -1):
                possiblities = memo[j]
                if s[i] == t[j]:
                    possiblities += memo[j + 1]
                new_memo[j] = possiblities
            memo = new_memo
        return memo[0]

    def numDistinct2(self, s: str, t: str) -> int:
        # dp(i, j) = at s[i:] and t[j:] how many distinct subsequence of s are equal to t?
        # dp(i, j)
        #   if s[i] and t[j] match, then += dp(i + 1, j + 1)
        #   += dp(i + 1, j)

        S, T = len(s), len(t)
        memo = [[0] * T for _ in range(S + 1)]

        for row in memo:
            row.append(1)

        for i in range(S - 1, -1, -1):
            for j in range(T - 1, -1, -1):
                possiblities = memo[i + 1][j]
                if s[i] == t[j]:
                    possiblities += memo[i + 1][j + 1]
                memo[i][j] = possiblities

        return memo[0][0]


s = Solution()
print(s.numDistinct("caaat", "cat"))
print(s.numDistinct("caat", "cat"))
print(s.numDistinct("caat", "ccat"))
