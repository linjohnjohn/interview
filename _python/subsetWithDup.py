# Problem: Subsets II
# Return every distinct subset of an integer array that may contain duplicates. Include the
# empty subset; result and element order do not matter.
#
# Expected input/output: nums=[1,2,2] -> [[],[1],[2],[1,2],[2,2],[1,2,2]]

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

# Key insight:
# Group equal values and choose 0 through their frequency copies of each; each count
# combination generates exactly one subset.
