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

