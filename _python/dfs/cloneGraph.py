from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node: Node):
            if node is None:
                return None

            if node not in visited:
                copy = Node(node.val, [])
                visited[node] = copy
                for n in node.neighbors:
                    copy.neighbors.append(dfs(n))
            
            return visited[node]
        
        return dfs(node)
    

