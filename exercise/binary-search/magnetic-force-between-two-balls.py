
class Solution(object):
    def isCan(self, position, m, current):
        pointer = position[0]
        result = 0
        n = len(position)
        for i in range(1, n):
            v = position[i]
            if v - pointer >= current:
                result += 1
                if result == m - 1:
                    return True
                pointer = v
        return False

            
    def maxDistance(self, position, m):
        position.sort()
        right = max(position)
        left = 1
        while left < right:
            mid = int((left + right) / 2)
            if self.isCan(position, m, mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
            


        
s = Solution()
# print(s.maxDistance([1,2,8,20,32], 3))
# print(s.maxDistance([79,74,57,22], 4))
# print(s.isCan([79,74,57,22], 4, 21))
# print(s.maxDistance([5,4,3,2,1,1000000000], 2))

