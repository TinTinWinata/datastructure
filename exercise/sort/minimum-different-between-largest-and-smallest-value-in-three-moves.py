class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4:
         return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans
        

s = Solution()
print(s.minDifference([1,5,0,10,14]))
# print(s.minDifference([5,3,2,4]))
# print(s.minDifference([6,6,0,1,1,4,6]))
# print(s.minDifference([82,81,95,75,20]))

# [82,81,95,75,20]
# [20,75,81,82,95]
