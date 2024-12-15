from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def countPercentage(_pass, total):
            return ((_pass + 1 ) / (total + 1)) - (_pass / total)
        percentages = [(-1 * countPercentage(v[0], v[1]), i) for i, v in enumerate(classes)]
        heapq.heapify(percentages)
        for _ in range(extraStudents):
            _, i = heapq.heappop(percentages)
            classes[i][0] += 1
            classes[i][1] += 1
            heapq.heappush(percentages, (-1 * countPercentage(classes[i][0], classes[i][1]), i))
        res = 0
        for v in classes:
            res += v[0] / v[1]
        return res / len(percentages)
            

print(Solution().maxAverageRatio([[1,2], [3,5], [2,2]], 2))