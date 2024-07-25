from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        leftP = 0
        rightP = n - 1
        res = 0
        nums.sort()
        # print(nums)
        while(leftP < rightP):
            v = nums[leftP] + nums[rightP]
            # print(f'left p {leftP} | right p {rightP} | v {v}')
            if v == k:
               res += 1
               leftP += 1
               rightP -= 1
            elif v < k:
                leftP += 1
            else:
                rightP -= 1
        return res

print(Solution().maxOperations([1,2,3,4], 5))
print(Solution().maxOperations([3,1,3,4,3], 6))