from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      def binarySearch(left: int, right: int) -> int:
         nonlocal nums
         if right <= left:
            return left
         mid = ((right - left) // 2) + left
         if (mid == 0 and nums[mid + 1] < nums[mid]) or (mid == len(nums) - 1 and nums[len(nums) - 1] < nums[mid]) or (nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]):
            return mid
         if(mid + 1 < len(nums) and nums[mid + 1] > nums[mid]):
            return binarySearch(mid + 1, right)
         if (mid -1 >= 0 and nums[mid - 1] > nums[mid]):
            return binarySearch(left, mid - 1)
      return binarySearch(0, len(nums) - 1)
    
print(Solution().findPeakElement([1]))