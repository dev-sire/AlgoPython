from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        columns = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    columns[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or columns[j] > 1):
                    ans += 1

        return ans