class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        memo = {}

        def dp(i, j, val=None):
            if i == M or j == N or i == -1 or j == -1:
                return 0

            curr = matrix[i][j]
            if val == None or curr > val:
                if (i, j) in memo:
                    return memo[(i, j)]
                else:
                    lip = (
                        max(
                            dp(i + 1, j, curr),
                            dp(i - 1, j, curr),
                            dp(i, j + 1, curr),
                            dp(i, j - 1, curr),
                        )
                        + 1
                    )
                    memo[(i, j)] = lip
                    return lip
            else:
                return 0

        mx = 0
        for i in range(M):
            for j in range(N):
                mx = max(dp(i, j), mx)

        return mx


matrix = [[5, 5, 3], [2, 3, 6], [1, 1, 1]]

s = Solution()
print(s.longestIncreasingPath(matrix))

matrix = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
print(s.longestIncreasingPath(matrix))

matrix = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
print(s.longestIncreasingPath(matrix))
matrix = [[2, 2, 2]]
print(s.longestIncreasingPath(matrix))
