from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        st = deque()
        for v in s:
            if v == "*":
                st.pop()
            else:
                st.append(v)
        return "".join(st)
        
print(Solution().removeStars("leet**cod*e"))