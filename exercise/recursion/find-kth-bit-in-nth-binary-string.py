class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(str: str):
            new_str = ""
            for v in str:
                new_str += "1" if v == "0" else "0"
            return new_str
        def recrusive(i):
            if i == 1: 
                return "0"
            before = recrusive(i - 1)
            return before + "1" + invert(before)[::-1]
        return recrusive(n)[k - 1]

print(Solution().findKthBit(3,1 ))
print(Solution().findKthBit(4, 11))