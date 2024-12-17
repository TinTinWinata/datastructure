from typing import List, Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        arr = [(-1 * ord(k), counter[k], k) for k in counter]
        heapq.heapify(arr)
        newStr = ""
        lastK = ""
        counterLastK = 0
        while arr:
            # print('before:', arr, f' last k : {lastK} | counter last k : {counterLastK}')
            o, v, k = heapq.heappop(arr)
            if k == lastK:
                counterLastK += 1
            else:
                counterLastK = 1 
            isRepeated = counterLastK > repeatLimit
            if isRepeated and len(arr) == 0:
               break
            elif isRepeated:
              #  print('IS REPEATED')
               o2, v2, k2 = heapq.heappop(arr)
               lastK = k2
               counterLastK = 1
               newStr += k2
               if v2 - 1 > 0:
                heapq.heappush(arr, (o2, v2 - 1 , k2))
            else:
              newStr += k
              lastK = k
            if isRepeated:
               heapq.heappush(arr, (o, v, k))
            elif v - 1 > 0:
              heapq.heappush(arr, (o, v - 1, k))
            # print('after:', arr)
            # print('-----')
        return newStr
# print(Solution().repeatLimitedString("cczazcc", 3))
print(Solution().repeatLimitedString("poppop", 2))