from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nFlowerbed = len(flowerbed)
        for i, v in enumerate(flowerbed):
            if v == 0 and (i - 1 < 0 or flowerbed[i - 1] == 0) and (i + 1 >= nFlowerbed or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    break
        return n <= 0
    
s = Solution()
# print(s.canPlaceFlowers([1,0,0,0,1], 1))
# print(s.canPlaceFlowers([1,0,0,0,1], 2))
print(s.canPlaceFlowers([1,0,0,0,0,1], 2))