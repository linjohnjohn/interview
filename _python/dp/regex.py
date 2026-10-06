class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s is string and p is regex express
        # 1. tokenize p
        # dp(i, j) = possible to match s[i:] and tokenized_p[j:]
        # dp(i, j) = dp(i + 1, j + 1) if characters "match"
        #         OR dp(i + 1, j)   if matches with *
        #       OR   dp(i, j + 1) if *
        # edge cases dp(i, P) = False, dp(S, i < P) = False, dp(S, P) = True

        S, P = len(s), len(p)

        tokens = []
        for i in range(P):
            if p[i] == "*":
                continue
            if i + 1 < P and p[i + 1] == "*":
                tokens.append((p[i], "*"))
            else:
                tokens.append((p[i], None))

        P = len(tokens)
        dp = [False] * P
        dp.append(True)

        for i in range(S - 1, -1, -1):
            next_dp = [False] * (P + 1)
            for j in range(P - 1, -1, -1):
                char, mod = tokens[j]
                matches = char == s[i] or char == "."
                zero_or_more = mod == "*"
                if matches and dp[j + 1]:
                    next_dp[j] = True
                    continue
                if matches and zero_or_more and dp[j]:
                    next_dp[j] = True
                    continue
                if zero_or_more and next_dp[j + 1]:
                    next_dp[j] = True
                    continue
            dp = next_dp

        return dp[0]


s = Solution()
print(s.isMatch("aa", "a"))

# print(s.isMatch("aa", ".b"))
# print(s.isMatch("aa", ".."))
# print(s.isMatch("nnn", "n*"))
