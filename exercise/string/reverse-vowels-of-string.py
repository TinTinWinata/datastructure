from collections import deque

class Solution:
    vowels = ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'I', 'O', 'U']
    def reverseVowels(self, s: str) -> str:
        temp = deque()
        sList = list(s)

        for v in sList:
            if v in self.vowels:
                temp.append(v)

        for i, v in enumerate(sList):
            if v in self.vowels:
                sList[i] = temp.pop()
        
        return "".join(sList)

s = Solution()
print(s.reverseVowels('aA'))  