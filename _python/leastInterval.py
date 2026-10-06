# Problem: Task Scheduler
# Each task takes one time unit. Identical task letters must have at least n intervening
# units, which may be other tasks or idle time. Return the minimum total time; tasks may be
# reordered.
#
# Expected input/output: tasks=['A','A','A','B','B','B'], n=2 -> 8; same tasks, n=0 -> 6

import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = {}
        cooldown = [None] * (n + 1)
        r, w = n, 0
        tasks_in_cooldown = 0
        counter = 0

        for l in tasks:
            if l not in freq:
                freq[l] = 1
            else:
                freq[l] += 1

        minheap = [-x for x in list(freq.values())]
        
        heapq.heapify(minheap)
        
        while minheap or tasks_in_cooldown > 0:
            counter += 1
            if minheap:
                v = -heapq.heappop(minheap)
                v -= 1
                
                if v > 0:
                    cooldown[r] = v
                    tasks_in_cooldown += 1

            nxt = cooldown[w]
            if nxt is not None:
                cooldown[w] = None
                heapq.heappush(minheap, -nxt)
                tasks_in_cooldown -= 1
            
            r = (r + 1) % (n + 1)
            w = (w + 1) % (n + 1)

        return counter
    
s = Solution()
print(s.leastInterval(['A', 'A', 'A', 'B', 'B'], 2))

# Key insight:
# Run the most frequent available task and hold unfinished tasks in a cooldown queue until
# eligible again; idle only when no task is available.
