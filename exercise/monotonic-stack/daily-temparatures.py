from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0 for _ in range(len(temperatures))]
        st = []
        for i, v in enumerate(temperatures):
            while len(st) > 0  and v > st[len(st)-1][0]:
                (_, popped_i) = st.pop()
                arr[popped_i] = i - popped_i
            st.append((v, i))
        return arr
    
print(Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))