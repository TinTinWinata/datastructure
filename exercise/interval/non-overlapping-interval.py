from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        right = intervals[0][1]
        result = 0
        for [num1, num2] in intervals[1:]:
            if num1 < right:
                result += 1
                right = min(right, num2)
            else:
                right = num2
        return result

# print(Solution().eraseOverlapIntervals([[0,1],[3,4],[1,2]]))
# print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
# print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(Solution().eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))