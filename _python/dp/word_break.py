# Problem: Word Break
# Decide whether s can be split into one or more dictionary words. Dictionary words may be
# reused.
#
# Expected input/output: s='leetcode', wordDict=['leet','code'] -> true; s='catsandog',
# wordDict=['cats','dog','sand','and','cat'] -> false

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        N = len(s)
        # O(m)
        MAX_WORD = max([len(w) for w in wordDict]) 
        memo = [None] * N
        memo.append(True)

        wordDict = set(wordDict)

        # O(n) dp problems
        def dp(i):
            if memo[i] != None:
                return memo[i]

            # O(t^2)
            for idx in range(i, min(N, i + MAX_WORD)):
                sub = s[i:idx + 1]
                if sub in wordDict:
                    if dp(idx + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dp(0)

s = Solution()

print(s.wordBreak("neetcodeneetcodeneetcodecodeneet", ["neet", "code"]))
print(s.wordBreak("catsincars", ["cats","cat","sin","in","cars"]))

# Key insight:
# Try dictionary prefixes at each position and memoize whether the remaining suffix can be
# segmented.
