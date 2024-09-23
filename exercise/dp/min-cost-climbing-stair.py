from typing import List

class Solution:
    def dfs(self, cost: List[int], current: int):
        if current < 0:
            return 0
        if self.dp[current] != -1:
            return self.dp[current]
        self.dp[current] = cost[current] + min(self.dfs(cost, current - 1), self.dfs(cost, current - 2))  
        return self.dp[current]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = [-1 for _ in range(len(cost))]
        return min(self.dfs(cost, len(cost) - 1), self.dfs(cost, len(cost) - 2))

print(Solution().minCostClimbingStairs([10,15,20]))