from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        adj = defaultdict(set)
        
        for w in words:
            for letter in w:
                adj[letter] = set()
                # adj[None].append(letter)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if w1 == w2:
                continue
            letter_idx = 0
            l1, l2 = None, None
            
            while l1 == l2:
                l1 = w1[letter_idx] if letter_idx < len(w1) else None
                l2 = w2[letter_idx] if letter_idx < len(w2) else None
                letter_idx += 1

            if l2 == None:
                return ''
            else:
                adj[l1].add(l2)


        def topological_sort(adj: dict[str, list]) -> list[str]:
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

        return ''.join(topological_sort(adj))
    

s = Solution()
print(s.foreignDictionary(["z","o"]))
print(s.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))
print(s.foreignDictionary(["abc","bcd","cde"]))
print(s.foreignDictionary(["wrtkj","wrt"]))
words=["abca","cab","cad"]
print(s.foreignDictionary(words))
