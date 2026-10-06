class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            findX, findY = find(x), find(y)
            if findX != findY:
                if rank[findX] >= rank[findY]:
                    parent[findY] = findX
                    rank[findX] += rank[findY]
                else:
                    parent[findX] = findY
                    rank[findY] += rank[findX]
                return True
            return False
        for [a, b] in edges:
            if not union(a - 1, b - 1):
                return [a, b]