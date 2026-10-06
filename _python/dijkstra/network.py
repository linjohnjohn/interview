from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((t, v))
        
        pq = [(0, k)]
        heapq.heapify(pq)
        visited = set()
    
        while pq:
            time, node = heapq.heappop(pq)

            if node not in visited:
                visited.add(node)
                if len(visited) == n:
                    return time

                for t, nei in adj[node]:
                    heapq.heappush(pq, (time + t, nei))
        
        return -1
    
s = Solution()

times = [[1, 2, 1], [1, 3, 1]]
print(s.networkDelayTime(times, 3, 1))
print(s.networkDelayTime(times, 3, 2))
times.append([2, 1, 10])
print(s.networkDelayTime(times, 3, 2))


            
        
        
