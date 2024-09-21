from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        for i, v in enumerate(senate):
            if v == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while len(r_queue) > 0 and len(d_queue) > 0:
            popped_r = r_queue.popleft()
            popped_d = d_queue.popleft()
            # radiant delete dire
            if popped_r < popped_d:
                r_queue.append(popped_r + len(senate))
            # dire delete radiant
            else:
                d_queue.append(popped_d + len(senate))
        if len(r_queue) <= 0:
            return "Dire"
        else:
            return "Radiant"



print(Solution().predictPartyVictory("RRDDRDDR"))