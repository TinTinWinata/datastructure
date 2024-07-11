class Solution(object):
    def recursive(self, v, arr, k):
        n = len(arr)
        if n == 1:
            return arr[0]
        v = (v + k - 1) % n
        del arr[v]
        return self.recursive(v, arr, k)

    def findTheWinner(self, n, k):
        arr = list(range(1, n + 1))
        return self.recursive(0, arr, k)
    
s = Solution()
print(s.findTheWinner(5, 2))
print(s.findTheWinner(6, 5))