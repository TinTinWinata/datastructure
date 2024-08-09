from collections import Counter
from math import floor
class Solution:
    def minimumPushes(self, word: str) -> int:
        map = {}
        res = 0
        list = Counter(word)
        sorted_list = sorted(list.items(), key=lambda x: x[1], reverse=True)
        for index, (key, value) in enumerate(sorted_list):
            counter = floor(index / 8) + 1
            map[key] = counter
        # print(map)
        for key, value in sorted_list:
            # print(f'{key} pushed : {value * map[key]} times')
            res += value * map[key]

        return res
                

# print(Solution().minimumPushes("abcb"))
# print(Solution().minimumPushes("abcde"))
# print(Solution().minimumPushes("xyzxyzxyzxyz"))
print(Solution().minimumPushes("aabbccddeeffgghhiiiiii"))