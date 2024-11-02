class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if len(sentence) == 1:
            return True
        arr = str.split(sentence, " ")
        for i in range(len(arr) - 1):
            if arr[i][-1] != arr[i+1][0]:
                return False
        if sentence[0] != sentence[-1]:
            return False
        return True
    
# print(Solution().isCircularSentence("the cat")) # False
print(Solution().isCircularSentence("leetcode exercises sound delightful"))  # True