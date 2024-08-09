from typing import List

class Solution:
    def recrusive(self, amount: int, coins: List[int], index: int):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if index <= 0:
            return 0
        return self.recrusive(amount, coins, index - 1) + self.recrusive(amount - coins[index - 1], coins, index)
    
    def change(self, amount: int, coins: List[int]) -> int:
        return self.recrusive(amount, coins, len(coins))

print(Solution().change(5, [1, 2, 3])) # 4