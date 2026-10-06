from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # create an adjacency list for each course where a directed edge a -> b means you need to finish b to take a
        # then iterate through each course in the adj list to see if any cycles are formed

        courseToPreq = {c: [] for c in range(numCourses)}
        prereqToCourse = {p: [] for p in range(numCourses)}

        for course, prereq in prerequisites:
            courseToPreq[course].append(prereq)
            prereqToCourse[prereq].append(course)
        


        topo = self.topological(courseToPreq)
        ktopo = self.kahn(prereqToCourse)
        print(topo, ktopo)
        return topo
    
    def kahn(self, preqToCourse: dict[int, list[int]]) -> list[int]:
        indegree = defaultdict(int)

        for p in preqToCourse.keys():
            indegree[p] = indegree[p]
            for c in preqToCourse[p]:
                indegree[c] += 1
        
        stack = []

        for c, i in indegree.items():
            if i == 0:
                stack.append(c)

        topo = []
        while stack:
            preq = stack.pop()
            topo.append(preq)
            for c in preqToCourse[preq]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    stack.append(c)
        
        if len(topo) == len(preqToCourse.keys()):
            return topo
        else:
            return []


    def topological(self, courseToPrereq: dict[int, list[int]]) -> list[int]:
        # keep track of courses we've already visited
        visited = set()
        # detect cycles
        completable = set()
        topo = []

        def dfs(i):
            if i in visited:
                return i in completable

            visited.add(i)
            prerequisites = courseToPrereq[i]

            for p in prerequisites:
                if not dfs(p):
                    return False
            
            topo.append(i)
            completable.add(i)
            return True


        for c in courseToPrereq.keys():
            if not dfs(c):
                return []
        
        return topo
    

s = Solution()

print(s.canFinish(2, [[0, 1], [1, 0]]))
print(s.canFinish(2, [[0, 1]]))
print(s.canFinish(3, [[0, 1], [1, 2]]))