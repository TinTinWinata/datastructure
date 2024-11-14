from typing import List
from math import ceil
import time

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(current: int):
            summed = 0
            for q in quantities:
                summed += ceil(q / current)
            # print(f'summed {summed} | current {current}')
            return summed <= n
        left, right = 1, max(quantities)
        result = 0
        while left <= right:
            mid = (right + left) // 2
            # print('left : ', left)
            # print('right : ', right)
            # print('mid : ', mid)
            if canDistribute(mid):
                result = mid
                right = mid - 1
                # print('can distribute!')
            else:
                left = mid  + 1
            #     print('cannot distribute!')
            # print('------------')
            # time.sleep(2)
        return result

# print(Solution().minimizedMaximum(2, [5,7]))
# print(Solution().minimizedMaximum(6, [11,6]))
print(Solution().minimizedMaximum(7, [15,10,10]))