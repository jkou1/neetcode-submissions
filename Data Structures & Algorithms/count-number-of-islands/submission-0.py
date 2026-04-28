class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        numislands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            
            while q:
                r1, c1 = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                
                for dr, dc in directions:
                    r = r1 + dr
                    c = c1 + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    numislands += 1
        
        return numislands