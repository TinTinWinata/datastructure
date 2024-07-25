from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        leftP = 0
        rightP = n - 1

        while(leftP < rightP):
            # Calculate
            res = max(res, abs(leftP - rightP) * min(height[leftP], height[rightP]))

            # Move Pointer
            if height[rightP] < height[leftP]:
                rightP -= 1
            else:
                leftP += 1
        
        return res
            
# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
# print(Solution().maxArea([1,1]))
print(Solution().maxArea([2,3,4,5,18,17,6]))