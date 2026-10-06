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