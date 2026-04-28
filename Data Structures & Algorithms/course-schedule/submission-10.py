from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_dict = defaultdict(list)

        for course, prereq in prerequisites:
            prereq_dict[course].append(prereq)

        visiting = set()
        visited = set()

        def recurse(course: int) -> bool:
            if course in visiting:
                return False  # found cycle

            if course in visited:
                return True   # already checked, no cycle

            visiting.add(course)

            for prereq in prereq_dict[course]:
                if not recurse(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not recurse(course):
                return False

        return True