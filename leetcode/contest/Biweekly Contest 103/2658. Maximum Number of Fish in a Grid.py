class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_fish = 0

        def dfs(r: int, c: int, visited: List[List[bool]]) -> int:
            if not (0 <= r < m and 0 <= c < n) or visited[r][c] or grid[r][c] == 0:
                return 0
            visited[r][c] = True
            fish = grid[r][c]
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                fish += dfs(r + dr, c + dc, visited)
            return fish

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    visited = [[False] * n for _ in range(m)]
                    max_fish = max(max_fish, dfs(r, c, visited))

        return max_fish
        