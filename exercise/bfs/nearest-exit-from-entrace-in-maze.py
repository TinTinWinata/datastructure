from typing import List
from collections import deque
STEPS = [[0,1], [1,0],[-1,0], [0,-1]]
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        queue.append((entrance, 0))
        n = len(maze)
        m = len(maze[0])
        visited = set()
        def is_valid(i, j):
            return (i >= 0 and j >= 0 and i < n and j < m) and maze[i][j] == '.'
        def is_end(i, j):
            return (i == 0 or i == n - 1 or j == m - 1 or j == 0) and maze[i][j] == '.' and not (i == entrance[0] and j == entrance[1])
        while queue:
            [i, j], steps = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if is_end(i, j):
                return steps
            for step in STEPS:
                new_i = i + step[0]
                new_j = j + step[1]
                if is_valid(new_i, new_j):
                    queue.append(([new_i, new_j], steps + 1))
        return -1


# print(Solution().nearestExit([[".","+"]], [0,0]))
# print(Solution().nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))
# print(Solution().nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))
print(Solution().nearestExit([["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+","+","."]], [0, 1]))