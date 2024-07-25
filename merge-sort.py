from typing import List

class Solution:
    # Splited array from merge sort method, will be combined / merged with the same order using 2 pointers
    def merge(self, leftNums: List[int], rightNums: List[int]) -> List[int]:
        i = 0
        j = 0
        newArray = []

        while i < len(leftNums) and j < len(rightNums):
            if leftNums[i] < rightNums[j]:
                newArray.append(leftNums[i])
                i += 1
            else:
                newArray.append(rightNums[j])
                j += 1
        
        while j < len(rightNums):
            newArray.append(rightNums[j])
            j += 1
        
        while i < len(leftNums):
            newArray.append(leftNums[i])
            i += 1
        return newArray 

    # Will be seperates 1 array into 2 array (left and right)
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sortedLeft = self.mergeSort(left)
        sortedRight = self.mergeSort(right)

        return self.merge(sortedLeft, sortedRight)


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    

# print(Solution().sortArray([5,2,3,1]))
# print(Solution().sortArray([5,1,1,2,0,0]))