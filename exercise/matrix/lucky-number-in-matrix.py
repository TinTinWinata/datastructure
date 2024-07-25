from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        maximums = []

        n = len(matrix)
        m = len(matrix[0])

        for i in range(m):
            temp = float('-inf')
            tempIndex = None
            for j in range(n):
                if matrix[j][i] > temp:
                    temp = matrix[j][i]
                    tempIndex = j
            maximums.append((temp, tempIndex))
        
        for (temp, tempIndex) in maximums:
            newTemp = float('+inf')
            for j in range(m):
                newTemp = min(newTemp, matrix[tempIndex][j])
            if newTemp == temp:
                result.append(temp)

        return result

print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))