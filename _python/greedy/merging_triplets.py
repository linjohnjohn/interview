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
