class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxarea = 0
        visited = set()

        def bfs(r, c) -> int:
            size = 0
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            size += 1
            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        size += 1
                        visited.add((r, c))
                        q.append((r, c))

            return size



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    size = bfs(r, c)
                    if maxarea < size:
                        maxarea = size
                    

        return maxarea
        