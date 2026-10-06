# Problem: Merge Triplets to Form Target Triplet
# A merge replaces one triplet by coordinate-wise maxima with another. Decide whether repeated
# merges can produce target.
#
# Expected input/output: triplets=[[2,5,3],[1,8,4],[1,7,5]], target=[2,7,5] -> true;
# triplets=[[3,4,5]], target=[2,4,5] -> false

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        a, b, c = target
        matches = 0
        for t in triplets:
            aa, bb, cc = t
            useable = aa <= a and bb <= b and cc <= c
            if useable:
                if a != None and a == aa:
                    matches += 1
                if b != None and b == bb:
                    matches += 1
                if c != None and c == cc:
                    matches += 1

                if matches == 3:
                    return True

        return matches == 3


# Key insight:
# Discard any triplet exceeding target in any coordinate. Among the rest, track separately
# whether each target coordinate can be reached; repeated matches of one coordinate do not
# replace missing coordinates.
