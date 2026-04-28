class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # 0 is empty, so ignore those
        # 1 is fresh fruit, need to get this count to 0 in order 
        # to return a time
        # if can't get # of 1s to 0, or if this ever stops decreasing,
        # then return -1. alternatively, we can just return nothing
        # if we can't find any fresh fruits to spread to atm
        rows, cols = len(grid), len(grid[0])
        rottingCoords = deque()
        visited = set()
        numFresh = 0

        def rotNeighbor(r, c):
            # we ultimately want to check that if we can't spread,
            # then did all fresh fruits turn to rot?
            # if so, then we return minMins
            nonlocal minMins
            nonlocal numFresh
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited 
                or grid[r][c] == 0):
                return
            else:
                grid[r][c] = 2
                rottingCoords.append([r, c])
                visited.add((r, c))
                numFresh -= 1


        # store coords of all rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rottingCoords.append([r, c])
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    numFresh += 1
        
        minMins = 0
        while rottingCoords and numFresh > 0:
            for coords in range(len(rottingCoords)):
                r, c = rottingCoords.popleft()

                rotNeighbor(r + 1, c)
                rotNeighbor(r -1, c)
                rotNeighbor(r, c + 1)
                rotNeighbor(r, c - 1)
            
            minMins += 1

        if numFresh == 0:
            return minMins
        else:   
            return -1