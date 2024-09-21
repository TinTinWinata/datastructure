from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = {}
        for v in arr:
            if v in arr_dict:
                arr_dict[v] += 1
            else:
                arr_dict[v] = 1
        occured_set = set()
        for v in arr_dict.values():
            if v in occured_set:
                return False
            occured_set.add(v)
        return True