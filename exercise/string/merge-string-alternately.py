class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        maxLen = max(lenWord1, lenWord2)

        def addWord(lenW, w, i):
            nonlocal res
            if i < lenW:
                res += w[i]

        for i in range(maxLen):
            addWord(lenWord1, word1, i)
            addWord(lenWord2, word2, i)
        
        return res
        
s = Solution()
print(s.mergeAlternately("abc", "pqr"))
print(s.mergeAlternately("ab", "pqrs"))