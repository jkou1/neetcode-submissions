class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        visited = set()

        rows, cols = len(grid), len(grid[0])


        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            curArea = 1
            while q:
                r, c = q.popleft()
                directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                for row, col in directions:
                    dr = r + row
                    dc = c + col
                    if(0 <= dr < rows and
                      0 <= dc < cols and
                      grid[dr][dc] == 1 and
                      (dr, dc) not in visited):
                        visited.add((dr, dc))
                        q.append((dr, dc))
                        curArea += 1
            return curArea



        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxArea = max(bfs(r, c), maxArea)


        return maxArea