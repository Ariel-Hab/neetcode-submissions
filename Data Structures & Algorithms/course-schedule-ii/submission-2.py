class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites or not prerequisites[0]:
            return [n for n in range(numCourses)]
        rows = len(prerequisites)
        cols = len(prerequisites[0])

        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
        # ahora tengo una lista ordenada por curso, y en cada pos los cursos que dependen de el
        
        state = [0]*numCourses

        response = []

        def has_loop(course:int)->bool:
            nonlocal response
            if state[course] == 2:
                return False
            if state[course] == 1:
                return True
            state[course] = 1
            for dep in adj[course]:
                if has_loop(dep):
                    return True
            state[course] = 2
            response.append(course)
            return False

        for course in range(numCourses):
            if state[course]==0 and has_loop(course):
                return []
        return response[::-1]


