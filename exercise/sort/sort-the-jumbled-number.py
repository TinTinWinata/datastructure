from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []
        for i, num in enumerate(nums):
            # 1. get mapped values and append to mapped
            v = str(num)
            temp = ""
            for c in v:
                temp += str(mapping[int(c)])
            mapped.append((int(temp), i))
        
        # 2. sort the nums based on the mapped
        newest = []
        mapped.sort(key=lambda x: x[0])
        for i in range(len(nums)):
            newest.append(nums[mapped[i][1]])

        return newest
        

print(Solution().sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))