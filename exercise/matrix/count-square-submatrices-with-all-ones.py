from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        count = 0
        max_side = min(n, m)
        for side in range(1, max_side + 1):
            for i in range(n - side + 1):
                for j in range(m - side + 1):
                    if all(matrix[i+x][j+y] == 1 for x in range(side) for y in range(side)):
                        # print(f'side: {side}, i: {i}, j: {j}')
                        count+=1
        return count

print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) # 15