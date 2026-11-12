from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # Build graph and record number of prerequisites for each course
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # Queue all courses that have 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken_courses = 0
        
        while queue:
            node = queue.popleft()
            taken_courses += 1
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If we could take all courses, no cycle existed
        return taken_courses == numCourses