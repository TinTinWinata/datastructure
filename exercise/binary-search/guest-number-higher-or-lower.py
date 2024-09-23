# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0

class Solution:
    def binarySearch(self, left: int, right: int) -> int:
        mid = ((right - left) // 2) + left
        if guess(mid) == 0:
            return mid
        elif guess(mid) > 0:
            return self.binarySearch(mid + 1, right)
        else:
            return self.binarySearch(left, mid - 1)
        
    def guessNumber(self, n: int) -> int:
        return self.binarySearch(1, n)