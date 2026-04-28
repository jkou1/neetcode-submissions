class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we have a list of prereqs, first item is a course,
        # everything that follows is it's prereqs
        # we can keep track of each course and it's prereqs in a dict
        crsDict = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            crsDict[c].append(p)
        # we can keep a set of all visited courses
        # but also need a set of all courses in the current cycle, aka we need to make sure we don't spot a course twice
        visited, cycle = set(), set()
        output = []

        # the main way to traverse all courses and their prereqs is dfs
        # why? bc we don't know by looking at any given course if we can take it,
        # need to go to the depth of all of it's prereqs, and their prereqs, etc
        # till we can guarentee that adding the course to our output list is possible

        def dfs(crs):
            # if crs is in cycle, return False, bc we cannot add it to schedule, can't continue
            if crs in cycle:
                return False
            if crs in visited:
                # if we visited this crs already, why continue? no need
                return True

            # now lets add this crs to cycle
            cycle.add(crs)
            # now we can look at the crs's prereqs, using this func recursively
            for pre in crsDict[crs]:
                if dfs(pre) == False:
                    return False
            # once we've verified that nothing is cyclical, add crs to visited, and to output
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output


