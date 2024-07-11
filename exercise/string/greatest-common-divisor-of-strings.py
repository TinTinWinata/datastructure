class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lenStr1 = len(str1)
        lenStr2 = len(str2)
        lowerStr = str2 if lenStr2 < lenStr1 or lenStr1 == lenStr2 else str1
        lowerLen = min(lenStr1, lenStr2)

        def checkDivisorPerworld(substr, word) -> bool:
            n = len(substr)
            nWord = len(word)
            if nWord % n != 0:
                return False
            for i in range(nWord // n):
                temp = word[i * n:i * n + n]
                if temp != substr:
                    return False
            return True

        def checkIsDivisor(substr) -> bool:
            nonlocal str1
            nonlocal str2
            return checkDivisorPerworld(substr, str1) and checkDivisorPerworld(substr, str2)
           

        res = ""
        for i in range(lowerLen):
            substr = lowerStr[:i+1]
            if checkIsDivisor(substr):
                res = substr
                
        return res
    
s = Solution()
print(s.gcdOfStrings("ABCABC", "ABC"))
print(s.gcdOfStrings("LEET", "CODE"))
print(s.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))

print("asd".size())