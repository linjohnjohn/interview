# Problem: Unique Paths
# Count paths from the top-left to bottom-right of an m-by-n grid, moving only right or down
# and with no obstacles.
#
# Expected input/output: m=3, n=7 -> 28; m=2, n=2 -> 2; m=1, n=5 -> 1

from collections import defaultdict
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)

    def uniquePaths2(self, m: int, n: int) -> int:
        coordToPaths = {}
        coordToPaths[(0, 0)] = 1

        while True:
            newPaths = defaultdict(int)
            for coord, paths in coordToPaths.items():
                r, c = coord
                if r + 1 < m:
                    newPaths[(r + 1, c)] += paths
                if c + 1 < n:
                    newPaths[(r, c + 1)] += paths
            if len(newPaths) != 0:
                coordToPaths = newPaths
            else:
                break

        return coordToPaths[(m - 1, n - 1)] 


s = Solution()
print(s.uniquePaths(2, 2))
print(s.uniquePaths(2, 4))
print(s.uniquePaths(10, 1))
                


# Key insight:
# Each cell's count is the sum from above and left. Equivalently, choose where the m-1 down
# moves occur among m+n-2 moves.
