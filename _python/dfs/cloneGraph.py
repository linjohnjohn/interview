# Problem: Clone Graph
# Given a node in a connected undirected graph, return a deep copy with the same values and
# edges. No cloned node may reuse an original node. Adjacency lists below describe neighbors
# by node label.
#
# Expected input/output: adjacency=[[2],[1]] -> a separate graph with adjacency [[2],[1]];
# node=None -> None

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
    



# Key insight:
# Map each original node to its clone before exploring neighbors, so cycles reuse the existing
# clone instead of recursing forever.
