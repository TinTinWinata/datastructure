class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([v.strip() for v in s.strip().split(' ') if v != ""][::-1])

print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("a good   example"))