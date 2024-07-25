from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res = float('-inf')
        temp = None
        def changeTemp(newTemp):
            nonlocal temp
            nonlocal res
            temp = newTemp
            res = max(res, newTemp)

        for i in range(0, n - k + 1):
            # Initiate First Calculate
            if temp is None:
                v = 0
                for j in range(k):
                    v += nums[i + j]
                changeTemp(v)
            else:
                v = temp - nums[i - 1] + nums[i + k - 1]
                changeTemp(v)
        return res / k

# print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
print(Solution().findMaxAverage([-1], 1))