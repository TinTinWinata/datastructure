from collections import deque

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        st = deque(s)
        for i in range(len(s)):
            st.rotate(1)
            if ''.join(st) == goal:
                return True
        return False
            
