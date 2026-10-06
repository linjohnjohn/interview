class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        level = [[]]

        for v in freq.keys():
            newLevel = []
            for set in level:
                for i in range(0, freq[v] + 1):
                    newSet = set.copy()
                    newSet.extend([v] * i) 
                    newLevel.append(newSet)
            level = newLevel
        return level
    

s = Solution()
print(s.subsetsWithDup([1 ,2 ,1, 2]))
print(s.subsetsWithDup([1, 1, 1]))
print(s.subsetsWithDup([1, 2, 3]))