# Problem: Islands and Treasure; Rotting Oranges
# islandsAndTreasure: Fill each INF land cell with its shortest four-direction distance to
# treasure (0), avoiding water (-1); unreachable land stays INF. orangesRotting: Each minute,
# rotten oranges (2) rot adjacent fresh ones (1); empty cells are 0. Return minutes to rot all
# fresh oranges, or -1.
#
# Expected input/output: treasure grid=[[0,INF],[-1,INF]] -> [[0,1],[-1,2]] (mutated); oranges
# grid=[[2,1,1],[1,1,0],[0,1,1]] -> 4; oranges grid=[[0]] -> 0

INF = 2147483647
class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        level = []
        distance = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    grid[r][c] = INF
                    level.append((r, c))

        
        while level:
            newLevel = []
            for r, c in level:
                if r >= ROWS or r < 0 or c >= COLS or c < 0:
                    continue

                if grid[r][c] == INF:
                    grid[r][c] = distance
                    newLevel.append((r + 1, c))
                    newLevel.append((r - 1, c))
                    newLevel.append((r, c + 1))
                    newLevel.append((r, c - 1))
            
            level = newLevel
            distance += 1

    # 0 representing an empty cell
    # 1 representing a fresh fruit
    # 2 representing a rotten fruit
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        level = []
        visited = set()
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    level.append((r, c))


        while level:
            newLevel = []
            hasNewRot = False
            for r, c in level:
                if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r,c) in visited:
                    continue

                if grid[r][c] == 1:
                    hasNewRot = True
                
                if grid[r][c] == 1 or grid[r][c] == 2:
                    visited.add((r,c))
                    newLevel.append((r + 1, c))
                    newLevel.append((r - 1, c))
                    newLevel.append((r, c + 1))
                    newLevel.append((r, c - 1))
            
            level = newLevel
            if hasNewRot:
                time += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    return -1
        return time

grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

s = Solution()

# s.islandsAndTreasure(grid)

fruit =[
    [1,1,0],
    [0,1,1],
    [0,1,2]
    ]


fruitImpossible =[
    [1,1,0],
    [0,1,1],
    [0,1,1],
    [1,0,2]
    ]

fruitImpossible2 =[
    [0]
    ]


print(s.orangesRotting(fruit))
print(s.orangesRotting(fruitImpossible))
print(s.orangesRotting(fruitImpossible2))


# Key insight:
# Start BFS from all treasures or rotten oranges at once. Each BFS layer is one distance step
# or minute; check for unreachable fresh oranges afterward.
