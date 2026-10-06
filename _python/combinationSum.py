# Problem: Combination Sum
# Given distinct positive candidates, return all unique combinations summing to target. Each
# candidate may be used any number of times; output order does not matter. Standard target is
# positive.
#
# Expected input/output: nums=[2,3,6,7], target=7 -> [[2,2,3],[7]]; nums=[2], target=3 -> []

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        if target == 0: return []
        level = [[target, []]]
        res = []

        for n in nums:
            newLevel = []
            for remainingTarget, combo in level:
                combo: list[int]
                multiple = 0
                while True:
                    v = remainingTarget - n * multiple
                    if v < 0:
                        break
                    newCombo = combo.copy()
                    newCombo.append(multiple)

                    if v == 0:
                        res.append(newCombo)
                    else:
                        newLevel.append([v, newCombo])

                    multiple += 1
                level = newLevel
        
        ans = []
        for r in res:
            a = []
            for idx, multiple in enumerate(r):
                a.extend([nums[idx]] * multiple)
            ans.append(a)

        return ans



s = Solution()                

print(s.combinationSum([2,5,6,9], 9))
print(s.combinationSum([2,5,6,9], 0))
print(s.combinationSum([2], 9))

# Key insight:
# Process candidates in a fixed order and choose how many copies of each to use; this avoids
# generating reordered duplicates.
