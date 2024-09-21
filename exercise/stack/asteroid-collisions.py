from typing import List
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = deque()
        asteroids_deque = deque(asteroids)
        is_first_not_minus = False
        while len(asteroids_deque) > 0:
            v = asteroids_deque.popleft()
            if v < 0 and is_first_not_minus and len(st)> 0:
                last = st[len(st) - 1]
                if last < 0:
                    st.append(v)  
                    continue
                v = abs(v)
                if v == last:
                    st.pop()
                elif v > last:
                    asteroids_deque.appendleft(-1 * v)
                    st.pop()
            else:
                if is_first_not_minus == False and v >= 0:
                    is_first_not_minus = True
                st.append(v)  
        return st

# print(Solution().asteroidCollision([5,10,-5]))
# print(Solution().asteroidCollision([8,-8]))
# print(Solution().asteroidCollision([10, 2, -5]))
# print(Solution().asteroidCollision([-2,-1,1,2]))
# print(Solution().asteroidCollision([-2,-1,1,-2]))
print(Solution().asteroidCollision([1,-2,-2,-2]))