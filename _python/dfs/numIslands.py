class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS = len(grid)
        if ROWS == 0:
            return 0
        COLS = len(grid[0])

        # iterate through every cell and if it's a 1, start exploring to see if it's neighbors are a 1 too, if so mark them 0s to claim them
        def dfs(i, j):
            # boundary check
            if i >= ROWS or i < 0 or j >= COLS or j < 0:
                return
            
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands
    
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        if ROWS == 0:
            return 0
        COLS = len(grid[0])

        # iterate through every cell and if it's a 1, start exploring to see if it's neighbors are a 1 too, if so mark them 0s to claim them
        # return size of this area visited by this exploration and sub-explorations
        def dfs(i, j):
            # boundary check
            if i >= ROWS or i < 0 or j >= COLS or j < 0:
                return 0
            
            area = 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                area += 1
                area += dfs(i + 1, j)
                area += dfs(i - 1, j)
                area += dfs(i, j + 1)
                area += dfs(i, j - 1)

            return area

        max_island = 0
        for i in range(ROWS):
            for j in range(COLS):
                max_island = max(dfs(i, j), max_island) 
        
        return max_island

s = Solution()

# grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# print(s.maxAreaOfIsland(grid))

# grid4 = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]

# print(s.maxAreaOfIsland(grid4))

grid6=[[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]

print(s.maxAreaOfIsland(grid6))
