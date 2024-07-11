class Solution(object):
    def getEncryptedString(self, s, k):
        res = ""
        n = len(s)
        for i in range(n):
            res += s[(i + k) % n]
        return res

s = Solution()
print(s.getEncryptedString("dart", 3))