MOD = 10**9+7
class Solution:
    def numTilings(self, n: int) -> int:
      dp = [-1 for _ in range(max(n + 1, 10))]
      dp[0] = 1
      dp[1] = 1
      dp[2] = 2
      def recrusive(n: int) -> int:
        nonlocal dp
        if dp[n] != -1:
           return dp[n]
        dp[n] = (2 * recrusive(n - 1) + recrusive(n - 3))
        return dp[n] % MOD 
      r = recrusive(n)
      return r
    
    