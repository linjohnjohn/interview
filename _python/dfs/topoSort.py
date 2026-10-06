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
