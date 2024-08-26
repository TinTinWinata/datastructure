from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # boards = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = 0
        n = rows * cols
        gap = 1
        results = [[rStart, cStart]]
        def check(i, j):
            nonlocal visited
            nonlocal results
            # nonlocal boards
            if visited >= n - 1:
                return
            if i >= 0 and j >= 0 and j < cols and i < rows:
                visited += 1
                results.append([i, j])
                # boards[i][j] = 1
                
                
        while visited < n - 1: 
            # time.sleep(1)
            # print('Visited : ', visited, ' N : ', n)
            for i in range(gap):
                # Check Right
                curr_i = rStart + i
                curr_j = cStart + gap
                # print('Coordinate : ', [curr_i, curr_j])
                check(curr_i, curr_j)
            for i in range(gap * 2 + 1):
                # Check Bottom
                curr_i = rStart + gap
                curr_j = cStart + gap - i
                check(curr_i, curr_j)
            for i in range(gap + (gap  - 1)):
                # Check Left
                curr_i = rStart + gap - 1 - i
                curr_j = cStart - gap
                check(curr_i, curr_j)
            for i in range(gap * 2 + 2):
                # Check Top
                curr_i = rStart - gap
                curr_j = cStart - gap + i
                check(curr_i, curr_j)
            # for b in boards:
            #   print(b)
            gap += 1
           
        return results  
            

# print(Solution().spiralMatrixIII(3, 3, 1,1 ))
# print(Solution().spiralMatrixIII(1, 4, 0,0))
# print(Solution().spiralMatrixIII(5, 6, 1, 4))