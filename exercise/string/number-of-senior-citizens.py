from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for v in details:
            if int(v[11]  + v[12]) > 60:
                res += 1
        return res

print(Solution().countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))