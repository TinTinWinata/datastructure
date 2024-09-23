from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        def dfs(index):
            if index < 0:
                return 0
            if dp[index] != -1:
                return dp[index]
            dp[index] = nums[index] + max(dfs(index - 2), dfs(index - 3))
            return dp[index]
        return max(dfs(len(nums) - 1), dfs(len(nums) - 2))

print(Solution().rob([1,2,3,1]))