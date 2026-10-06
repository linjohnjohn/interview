# Problem: Topological Sort (Helper Snippet)
# Given directed adjacency lists, return an ordering where every node appears before its
# outgoing neighbors; return [] if a cycle exists. This file is an extracted helper snippet
# rather than a standalone solution.
#
# Expected input/output: adj={'a':['b'],'b':['c'],'c':[]} -> ['a','b','c'];
# adj={'a':['b'],'b':['a']} -> []

def topological_sort(adj: dict[str, list]) -> list[str]:
    # perform dfs and keep track of when a node is "done"
    # reverse done list

    # visited set to ensure no
    visited = set()
    has_no_cycles = defaultdict(lambda: False)
    done_list = []

    def dfs(node: str):
        if node in visited:
            return has_no_cycles[node]

        visited.add(node)
        for child in adj[node]:
            # if there is a cycle return False
            if not dfs(child):
                return False

        done_list.append(node) if node is not None else None
        has_no_cycles[node] = True
        return True

    for letter in adj.keys():
        if not dfs(letter):
            return []

    done_list.reverse()
    return done_list


return "".join(topological_sort(adj))


# Key insight:
# DFS appends nodes only after their descendants finish, so reverse that completion order.
# Reaching a node still being explored detects a cycle.
