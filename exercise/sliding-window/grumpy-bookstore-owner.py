class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        max_sum = 0
        pointer = 0
        for i in range(n - minutes + 1):
            temp = 0
            for j in range(minutes):
                if grumpy[i + j] == 1:
                    temp += customers[i + j]
            if temp > max_sum:
                pointer = i
                max_sum = temp
        
        for i in range(minutes):
            grumpy[pointer + i] = 0

        result = 0
        for i in range(n):
            result += customers[i] if grumpy[i] == 0 else 0
        
        return result
        
s = Solution()

# print(s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
print(s.maxSatisfied([5, 8], [0,1], 1))