class Solution:
    def recrusive(self, n) -> int:
        if n in self.dp:
            return self.dp[n]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        self.dp[n] = self.recrusive(n - 3) + self.recrusive(n - 2) + self.recrusive(n - 1)
        return self.dp[n]
    def tribonacci(self, n: int) -> int:
        self.dp = {}
        return self.recrusive(n)