class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqs = {i: [] for i in range(numCourses)}

        for course, prereqcourse in prerequisites:
            prereqs[course].append(prereqcourse)

        visited = set()

        def dfs(prereq):
            if prereq in visited:
                return False
            if prereqs[prereq] == []:
                return True

            visited.add(prereq)

            for value in prereqs[prereq]:
                if not dfs(value):
                    return False

            visited.remove(prereq)
            prereqs[prereq] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True