from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return nums
        
        left_p = 0
        right_p = 1

        while left_p < n:
            if nums[left_p] == 0:
                if right_p < left_p:
                    right_p = left_p
                while right_p < n:
                    if nums[right_p] != 0:
                        break
                    else:
                      right_p += 1
                # print(f'left p : {left_p} | right p : ', right_p)
                if right_p < n and nums[right_p] != 0:
                    # print(f'Swapping {left_p} and {right_p} | Before Swap : ', nums)
                    nums[left_p], nums[right_p] = nums[right_p], nums[left_p]
                    right_p += 1
                if right_p >= n:
                    break
            left_p += 1

arr = [4,2,4,0,0,3,0,5,1,0]
Solution().moveZeroes(arr)

print('Result : ', arr)