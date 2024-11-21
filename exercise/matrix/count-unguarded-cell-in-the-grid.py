from typing import List

CELL_NOTHING = -1
CELL_WALL = 0
CELL_GUARD = 1
CELL_GUARDED = 2
INCREMENTOR = [[0, 1], [1, 0], [-1, 0], [0 ,-1]]
BASE_INCREMENTOR = [[0, 1], [1, 0], [-1, 0], [0 ,-1]]

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        matrix = [[CELL_NOTHING for _ in range(n)] for _ in range(m)]
        
        for [i, j] in guards:
            matrix[i][j] = CELL_GUARD
        for [i, j] in walls:
            matrix[i][j] = CELL_WALL

        def is_valid_cell(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and (matrix[i][j] == CELL_NOTHING or matrix[i][j] == CELL_GUARDED)
        for [i, j] in guards:
            for k, [incI, incJ] in enumerate(INCREMENTOR):
              while(is_valid_cell(i + incI, j + incJ)):
                  matrix[i + incI][j + incJ] =  CELL_GUARDED
                  incI += BASE_INCREMENTOR[k][0]
                  incJ += BASE_INCREMENTOR[k][1]
        unguarded_count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == CELL_NOTHING:
                    unguarded_count += 1
        return unguarded_count

print(Solution().countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))
# print(Solution().countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]))