# Problem: Surrounded Regions
# In an X/O board, change every O region not connected to a border into X. Connections use
# four directions. Modify the board in place.
#
# Expected input/output: board=[['X','X','X'],['X','O','X'],['X','X','X']] -> all X;
# board=[['O','O'],['X','O']] -> unchanged

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        level = []

        for i in range(ROWS):
            if board[i][0] == "O":
                level.append((i, 0))
            if board[i][COLS - 1] == "O":
                level.append((i, COLS - 1))


        for i in range(COLS):
            if board[0][i] == "O":
                level.append((0, i))
            if board[ROWS - 1][i] == "O":
                level.append((ROWS - 1, i))
        

        while level:
            newLevel = []
            for r, c in level:
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    continue

                if board[r][c] == "O":
                    board[r][c] = "T"
                    newLevel.append((r + 1, c))
                    newLevel.append((r - 1, c))
                    newLevel.append((r, c + 1))
                    newLevel.append((r, c - 1))
            
            level = newLevel
        

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"

grid = [
    ["X", "X", "X"],
    ["X", "O", "X"],
    ["X", "X", "X"],
]

s = Solution()

s.solve(grid)

print(grid)

grid = [
    ["X", "X", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "X", "X"]
]

s.solve(grid)

print(grid)

# Key insight:
# Mark all O cells reachable from border O cells as safe; flip unmarked O cells and restore
# the safe ones.
