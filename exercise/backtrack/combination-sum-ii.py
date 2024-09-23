
from typing import List
class Solution:
    def dfs(self, current: int, value: int, target: int, arr: List[int], k: int):
        if value == target and len(arr) == k:
            self.results.append(arr)
            return
        if current >= 10 or value > target or len(arr) > k:
            return
        for i in range(current + 1, 10):
            new_arr = arr.copy()
            new_arr.append(i)
            self.dfs(i, value + i, target, new_arr, k)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.results = []
        self.dfs(0, 0, n, [], k)
        return self.results
    
# print(Solution().combinationSum3(3, 7))
print(Solution().combinationSum3(3, 9))