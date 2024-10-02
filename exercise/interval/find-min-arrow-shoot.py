from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        # [[1,6],[2,8],[7,12],[10,16]]
        right = points[0][1]
        count = 0
        for [num1, num2] in points[1:]:
            if num1 <= right:
                count += 1
                right = min(right, num2)
            else:
                right = num2
        return len(points) - count
    
print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))