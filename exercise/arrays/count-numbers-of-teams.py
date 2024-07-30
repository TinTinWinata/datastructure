from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        result = 0 
        prefixCountAsc = [0] * len(rating)
        prefixCountDesc = [0] * len(rating)

        for i in range(1, len(rating)):
            for j in range(i - 1, -1, -1):
                isAscending = rating[j] > rating[i]
                if isAscending:
                    prefixCountAsc[i] += 1
                else:
                    prefixCountDesc[i] += 1

        # print('Prefix Count Ascending : ', prefixCountAsc)
        # print('Prefix Count Descending : ', prefixCountDesc)
        
        for i in range(2, len(rating)):
            for j in range(i - 1, 0, -1):
                isAscending = rating[j] > rating[i]
                if isAscending:
                    result += prefixCountAsc[j]
                else:
                    result += prefixCountDesc[j]
 
        return result
    
print(Solution().numTeams([1,2,3]))