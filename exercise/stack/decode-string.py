from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        st = deque()
        for v in s:
            if v == "]":
                arr = []
                while True:
                    popped = st.pop()
                    if popped == "[":
                        # we find the times
                        times_arr = []
                        while True:
                            if len(st) == 0:
                                break
                            times_v = st[len(st) - 1]
                            if(ord(times_v) <= 57 and ord(times_v) >= 48):
                                times_arr.append(st.pop())
                            else:
                                break
                            
                        times = int("".join(times_arr[::-1]))
                        reversed_arr = arr[::-1]
                        for i in range(times):
                            for reversed_v in reversed_arr:
                                st.append(reversed_v)
                        break
                    else:
                        arr.append(popped)
            else:
                st.append(v)
        return "".join(st)

# print(Solution().decodeString("3[a]2[bc]"))
# print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("100[leetcode]"))