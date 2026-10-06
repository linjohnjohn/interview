# Problem: Edit Distance
# Return the fewest single-character insertions, deletions, and replacements needed to turn
# word1 into word2.
#
# Expected input/output: word1='horse', word2='ros' -> 3; word1='', word2='abc' -> 3

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp(i, j) = edit distance from word1[i:] to word2[j:]
        # dp(i, j) = min of:
        #               dp(i + 1, j + 1) if characters match
        #               dp(i + 1, j) + 1 delete
        #               dp(i, j + 1) + 1 insert
        #               dp(i + 1, j + 1) + 1 replace
        M, N = len(word1), len(word2)
        memo = [[None] * N for _ in range(M)]
        memo.append([N - n for n in range(N)])

        # w1 = monk => M = 4 w2 = money N = 5
        for m in range(M + 1):
            memo[m].append(M - m)

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if word1[r] == word2[c]:
                    memo[r][c] = memo[r + 1][c + 1]
                else:
                    memo[r][c] = (
                        min(memo[r + 1][c], memo[r][c + 1], memo[r + 1][c + 1]) + 1
                    )
        return memo[0][0]


s = Solution()
print(s.minDistance("monkeys", "money"))
print(s.minDistance("abc", "cbabc"))


# Key insight:
# For matching characters, advance both strings for free. Otherwise take 1 plus the cheapest
# insert, delete, or replace subproblem.
