from collections import deque
from typing import List 

STEPS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        n = len(grid)
        m = len(grid[0])
        oranges_count = 0
        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                if v == 2 or v == 1:
                    oranges_count += 1
                if v == 2:
                    queue.append(([i, j], 0))
        def is_valid(i, j):
            return i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == 1
        max_level = 0
        while queue:
            [i, j], level = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            max_level = max(max_level, level)
            for step in STEPS:
                new_i = i + step[0]
                new_j = j + step[1]
                if is_valid(new_i, new_j):
                    queue.append(([new_i, new_j], level + 1))
        return max_level if len(visited) == oranges_count else -1 
        
