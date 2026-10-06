# Problem: Graph Valid Tree
# Given n nodes labeled 0..n-1 and undirected edges, decide whether the graph is a tree:
# connected and without cycles.
#
# Expected input/output: n=5, edges=[[0,1],[0,2],[0,3],[1,4]] -> true; n=3,
# edges=[[0,1],[1,2],[2,0]] -> false

from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        nodeToGroup = defaultdict(set)
        for i in range(n):
            nodeToGroup[i] = { i }
        
        for [a, b] in edges:
            groupA = nodeToGroup[a]
            groupB = nodeToGroup[b]
            if nodeToGroup[a] == nodeToGroup[b]:
                continue

            smaller, larger = None, None

            if len(groupA) < len(groupB):
                smaller = groupA
                larger = groupB
            else:
                smaller = groupB
                larger = groupA
            
            larger.update(smaller)

            nodeToGroup[a] = larger
            nodeToGroup[b] = larger

        
        return len(nodeToGroup[0]) == n
    


s = Solution()

print(s.validTree(2, [[0, 1]]))
print(s.validTree(4, [[0, 1], [0, 2]]))
print(s.validTree(4, [[0, 1], [0, 2], [3, 2]]))
print(s.validTree(4, [[0, 1], [0, 2], [2, 1]]))



# Key insight:
# A tree has exactly n-1 edges and is connected. Check connectivity with DFS or union-find;
# union-find can also reject an edge within an existing component.
