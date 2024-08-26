import time
from typing import List, Set, Tuple

class Solution:
    def checkMagicSquare(self, grid: List[List[int]], i: int, j: int) -> bool:
        temp_set = set()
        for x in range(3):
            for y in range(3):
                if grid[i+x][j+y] in temp_set or grid[i+x][j+y] < 1 or grid[i+x][j+y] > 9:
                    return False
                temp_set.add(grid[i+x][j+y])
        temp_sum = sum(grid[i][j:j + 3]) 
        if temp_sum != sum(grid[i+1][j:j+3]):
            return 
        temp_sum = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        if temp_sum != grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]:
            return
        temp_sum = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
        if temp_sum != grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]:
            return
        self.res +=1 
        return True
    
    def dfs(self, grid: List[List[int]], i: int, j: int, max_i: int, max_j: int, visited: Set[Tuple[int]]) -> bool:
        if i + 2 >= max_i or j + 2 >= max_j or (i, j) in visited:
          return
        
        visited.add((i, j))
        self.checkMagicSquare(grid, i, j)

        self.dfs(grid, i + 1, j, max_i, max_j, visited)
        self.dfs(grid, i, j + 1, max_i, max_j, visited)
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        max_i = len(grid)
        max_j = len(grid[0])
        
        if max_i < 3 or max_j < 3:
            return 0
        
        self.res = 0
        curr_i = 0
        curr_j = 0

        visited = set()

        self.dfs(grid, curr_i, curr_j, max_i, max_j, visited)
        return self.res
        

# print(Solution().numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
# print(Solution().numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]]))
print(Solution().numMagicSquaresInside([[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]))