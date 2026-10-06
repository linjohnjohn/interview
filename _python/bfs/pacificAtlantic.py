# Problem: Pacific Atlantic Water Flow
# Return cells from which water can flow to both oceans using four-direction moves to equal or
# lower heights. Pacific touches the top/left edges; Atlantic touches bottom/right. Output
# coordinate order does not matter.
#
# Expected input/output: heights=[[1,2],[4,3]] -> [[0,1],[1,0],[1,1]]; heights=[[1]] ->
# [[0,0]]

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacReachable = [[True if i == 0 or j == 0 else None for i in range(COLS)] for j in range(ROWS)]
        atlReachable = [[True if i == COLS - 1 or j == ROWS - 1 else None for i in range(COLS)] for j in range(ROWS)]

        self.is_reachable(heights, pacReachable)
        self.is_reachable(heights, atlReachable)

        # print(pacReachable)
        # print(atlReachable)
        ans = []
        for r in range(ROWS):
            for c in range(COLS): 
                if pacReachable[r][c] and atlReachable[r][c]:
                    ans.append([r, c])
        
        return ans

    # BFS from multi source
    def is_reachable(self, heights, reachable):
        ROWS, COLS = len(heights), len(heights[0])
        level = []

        for r in range(ROWS):
            for c in range(COLS):
                if reachable[r][c]:
                    reachable[r][c] = None
                    level.append((r, c, 0))
        
        while level:
            newLevel = []
            for r, c, neighbor_val in level:
                # bounds check
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    continue
                # r,c already visited
                if reachable[r][c]:
                    continue
                # not tall enough flow downwards
                if heights[r][c] < neighbor_val:
                    continue

                reachable[r][c] = True
                curr = heights[r][c]
                newLevel.append((r + 1, c, curr))
                newLevel.append((r - 1, c, curr))
                newLevel.append((r, c + 1, curr))
                newLevel.append((r, c - 1, curr))
            level = newLevel
        


s = Solution()
grid = [
    [0, 1, 0, 1],
    [1, 2, 5, 1],
    [1, 0, 2, 2],
    [1, 1, 1, 1]
]
print(s.pacificAtlantic(grid))

grid = [
    [1]
]
print(s.pacificAtlantic(grid))

grid = [
    [1, 1],
    [1, 0]
]
print(s.pacificAtlantic(grid))


# Key insight:
# Reverse the flow: search uphill from each ocean's edges, then intersect their reachable cell
# sets.
