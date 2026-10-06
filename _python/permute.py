# Problem: Permutations
# Given distinct integers, return every ordering that uses each number exactly once. Result
# order does not matter.
#
# Expected input/output: nums=[1,2] -> [[1,2],[2,1]]; nums=[1] -> [[1]]

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # 1. Choose a number to go first place into current array
        # 2. Then choose another number and recurse
        ans = []
        def backtrack(current: list[int], remainder: list[int]):
            if remainder:
                for i in range(0, len(remainder)):
                    v = remainder[i]
                    current.append(v)
                    remainder.pop(i)
                    backtrack(current, remainder)
                    remainder.insert(i, v)
                    current.pop()
            else:
                ans.append(current.copy())

        backtrack([], nums)
        return ans

s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([1]))
print(s.permute([]))

# Key insight:
# Backtrack by choosing an unused number for the next position, then undo that choice before
# exploring another branch.
