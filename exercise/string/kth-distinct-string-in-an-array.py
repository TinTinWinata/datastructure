from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
            arr_counter = Counter(arr)
            for key in arr_counter:
                  if arr_counter[key] == 1:
                        k -= 1
                        if k == 0:
                              return key 
            return ""

print(Solution().kthDistinct(["a", "b", "c", "a", "b", "d"], 2)) 