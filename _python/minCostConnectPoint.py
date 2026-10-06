class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # add all possible edges into a min heap (cost, a, b)
        # run union find to connect all points with min cost
        N = len(points)
        min_edges = []
        for index, (x1, y1) in enumerate(points):
            for j in range(index + 1, N):
                x2, y2 = points[j]
                min_edges.append((abs(x1 - x2) + abs(y1 - y2), index, j))
        
        min_edges.sort()

        uf = UnionFind(N)

        total = 0
        for cost, a, b in min_edges:
            if uf.union(a, b):
                total += cost

        return total
    
class UnionFind:
    def __init__(self, N) -> None:
        self.N = N
        self.parent = list(range(N))
        self.rank = [1] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        pX = self.find(x)
        pY = self.find(y)

        if pX == pY:
            return False
        elif self.rank[pX] > self.rank[pY]:
            self.parent[pY] = pX
            self.rank[pX] += self.rank[pY]
        else:
            self.parent[pX] = pY
            self.rank[pY] += self.rank[pX]
        return True
    

s = Solution()
print(s.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]]))
print(s.minCostConnectPoints([[0,0],[1, 1]]))
print(s.minCostConnectPoints([[0,0]]))
print(s.minCostConnectPoints([[0,0], [0, 1], [1, 0]]))