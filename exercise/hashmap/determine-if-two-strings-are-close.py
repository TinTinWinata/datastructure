from typing import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_counter = Counter(word1)
        word2_counter = Counter(word2)
        same_key_set = set()
        same_value_counter = dict()

        for key in word1_counter.keys():
            same_key_set.add(key)
            v = word1_counter[key]
            if v in same_value_counter:
                same_value_counter[v] += 1
            else:
                same_value_counter[v] = 1

        for key in word2_counter.keys():
            v = word2_counter[key]
            if v not in same_value_counter:
                return False
            same_value_counter[v] -= 1
            if key not in same_key_set or same_value_counter[v] < 0:
                return False
            
        return True
    
s = Solution()
# print(s.closeStrings("cabbba", "abbccc"))
print(s.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))
        