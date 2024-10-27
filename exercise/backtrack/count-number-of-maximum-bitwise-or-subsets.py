import time
from typing import List, Set

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
      dict_res = {}
      max_res = 0
      def calculate_or(arr: List[int]): 
         res = 0
         for v in arr:
            res = res | v
         return res
      
      def dfs(arr: List[int], curr_idx: int):
          nonlocal nums, max_res
          # print(f'curr_idx {curr_idx} | ' ,arr)
          res = calculate_or(arr)
          if res in dict_res:
            dict_res[res] += 1
          else:
            dict_res[res] = 1
          max_res = max(dict_res[res], max_res)
          for i in range(curr_idx, len(nums)):
              new_arr = arr.copy()
              new_arr.append(nums[i])
              dfs(new_arr, i + 1)
      dfs([], 0)
      return max_res

print(Solution().countMaxOrSubsets([3, 2, 1, 5]))