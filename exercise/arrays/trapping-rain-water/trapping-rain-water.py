class Solution(object):
    def trap(self, height):
        n = len(height)
        h = 0
        arr_l = [0] * n
        arr_r = [0] * n
        for i, v in enumerate(height):
            if v > h:
                h = v
            arr_l[i] = h
        h = 0
        for i in range(n):
            j = n - i - 1
            if height[j] > h:
                h = height[j]
            arr_r[j] = h
        result = 0
        for i in range(n):
            result += min(arr_l[i], arr_r[i]) - height[i]
        return result
            
        

s = Solution()
print('Result : ', s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))