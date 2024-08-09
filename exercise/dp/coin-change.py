from typing import List

class Solution:
    def recrusive(self, amount: int, coins: List[int], index: int, dp):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if (amount, index) in dp:
            return dp[(amount, index)]
        if index <= 0:
            return 0
        dp[(amount, index)] =  self.recrusive(amount, coins, index - 1, dp) + self.recrusive(amount - coins[index - 1], coins, index, dp)
        return dp[(amount, index)]
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        return self.recrusive(amount, coins, len(coins), dp)

print(Solution().change(5, [1, 2, 3])) # 4