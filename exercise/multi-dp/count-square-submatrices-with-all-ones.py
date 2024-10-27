from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        count = 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                  if i == 0 or j == 0:
                      dp[i][j] = 1
                  else:
                      dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                  count += dp[i][j]
        return count

print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) # 15