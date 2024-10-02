from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # arr : [37,12,28,9,100,56,80,5,12]
        # Sorted arr : [5,9,12,12,28,37,56,80,100]
        map = {}
        i = 0
        for v in sorted(arr):
            if v not in map:
              i += 1
              map[v] = i
                
        result = [map[arr[i]] for i in range(len(arr))]
        return result

# print(Solution().arrayRankTransform([40,10,20,30])) # [4,1,2,3]
print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12])) 