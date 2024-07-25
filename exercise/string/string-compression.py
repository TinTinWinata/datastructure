from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        index = 0
        temp = chars[0]
        n = len(chars)
        temp_res = 1
        def add(v):
            nonlocal index
            chars[index] = v
            index += 1

        def check_add_length():
            nonlocal temp_res
            if temp_res > 1:
                for temp_v in str(temp_res):
                    add(temp_v)
                temp_res = 1

        for i in range(1, n):
            v = chars[i]
            if v == temp:
                temp_res += 1
            if v != temp:
                add(temp)
                check_add_length()
                temp = v
            if i == n - 1:
                add(v)
                check_add_length()
        return index


res = ["a", "b", "c"]
print(Solution().compress(res))
print('After : ', res)

res = ["a","a","b","b","c","c","c"]
print(Solution().compress(res))
print('After : ', res)