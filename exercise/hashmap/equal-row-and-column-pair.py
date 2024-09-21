from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        for i in range(n):
            row_hash = "#".join([str(grid[x][i]) for x in range(n)])
            for j in range(n):
                col_hash = "#".join([str(grid[j][x]) for x in range(n)])
                if row_hash == col_hash:
                    result += 1
        return result

s = Solution()
print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))