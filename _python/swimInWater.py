# Problem: Swim in Rising Water
# At time t, cells with elevation at most t are traversable. Return the earliest time you can
# move from top-left to bottom-right using four directions.
#
# Expected input/output: grid=[[0,2],[1,3]] -> 3; grid=[[0]] -> 0

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # bfs with binary search
        # bfs keeping track of max water 

# Key insight:
# Minimize the highest elevation on a path using a min-heap search, or binary-search a time
# threshold and test reachability. The current solution is a stub.
