class Solution(object):
    def threeConsecutiveOdds(self, arr):
        n = len(arr)
        if n < 3:
            return False
        for i, v in enumerate(arr):
            if i + 2 >= n:
                break
            if v % 2 != 0:
                is_odds = True
                for j in range(2):
                    if arr[i + j + 1] % 2 == 0:
                        is_odds = False
                        break
                if is_odds:
                    return True
        return False
    
s = Solution()
# print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
print(s.threeConsecutiveOdds([1,2,1,1]))