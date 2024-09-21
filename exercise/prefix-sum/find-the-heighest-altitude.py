from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain_sum = max_gain_sum = 0
        for v in gain:
            gain_sum += v
            max_gain_sum = max(max_gain_sum, gain_sum)
        return max_gain_sum