class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seenTiles = set()

        def checkCorners(i, j):
            if (i, j) in seenTiles or (i < 0 or i > len(grid) - 1) or (j < 0 or j > len(grid[0]) - 1):
                return 0
            curTile = grid[i][j]
            if curTile == 0:
                seenTiles.add((i, j))
                return 0
            else:
                # check corners recursively
                seenTiles.add((i, j))
                # check if the corners are in bounds
                return (1 + checkCorners(i + 1, j) + 
                checkCorners(i - 1, j) + 
                checkCorners(i, j + 1) + 
                checkCorners(i, j - 1))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seenTiles:
                    maxArea = max(maxArea, checkCorners(i, j))

        return maxArea