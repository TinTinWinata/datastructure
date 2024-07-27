import heapq
class Solution(object):
    def longestSubarray(self, nums, limit):
        lp = 0
        rp = 0
        n = len(nums)
        res = 0

        # Sliding windows
        min_arr = []
        max_arr = []

        while lp < n:
            heapq.heappush(min_arr, nums[rp])
            heapq.heappush(max_arr, -1 * nums[rp])
            temp_res = abs(-1 * max_arr[0] -  min_arr[0])
            # print('min arr : ', min_arr)
            # print('temp res : ', temp_res, ' rp : ', rp, ' lp : ', lp)
            if temp_res <= limit and rp - lp + 1 > res:
                res = rp - lp + 1

            rp += 1
            if rp >= n:
                min_arr = []
                max_arr = []
                lp += 1
                rp = lp
        return res
        
        
s = Solution()
print(s.longestSubarray([8,2,4,7], 4))