class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'u', 'o'])
        temp = 0
        n = len(s)

        def isInVowels(v):
            nonlocal vowels
            return v in vowels
        
        
        for i in range(k):
            if isInVowels(s[i]):
                temp += 1

        res = temp
        for i in range(1, n - k + 1):
            if isInVowels(s[i - 1]):
                temp -= 1
            if isInVowels(s[i + k - 1]):
                temp += 1
            res = max(res, temp)
        return res
    
# print(Solution().maxVowels("abciiidef", 3))
print(Solution().maxVowels("ibpbhixfiouhdljnjfflpapptrxgcomvnb", 33))