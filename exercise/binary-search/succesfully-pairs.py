from typing import List

class Solution:
    def binarySearch(self,arr,  left, right, spell, success) -> int:
        if right <= left:
            return left if arr[left] * spell >= success else left + 1
        mid = ((right - left) // 2) + left
        if arr[mid] * spell >= success:
            return self.binarySearch(arr, left, mid - 1, spell, success)
        else:
            return self.binarySearch(arr, mid + 1, right, spell, success)

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        results = []
        for spell in spells:
            left = self.binarySearch(potions, 0, len(potions) - 1, spell, success)
            results.append(len(potions) - left)
        return results
    
print(Solution().successfulPairs([5,1,3], [1,2,3,4,5], 7))