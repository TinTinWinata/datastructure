from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('+inf')
        second = float('+inf')
        for v in nums:
            if v <= first:
                first = v
            elif v <= second:
                second = v
            else:
                return True
        return False


# print(Solution().increasingTriplet([1,2,3,4,5]))
# print(Solution().increasingTriplet([5,4,3,2,1]))
# print(Solution().increasingTriplet([2,1,5,0,4,6]))
print(Solution().increasingTriplet([2,4,-2,-3]))