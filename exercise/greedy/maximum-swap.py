import heapq
from collections import Counter

class Solution:
    def maximumSwap(self, num: int) -> int: # 98368
        arr = list(str(num))
        dict_index = {}
        for i, v in enumerate(arr):
            dict_index[int(v)] = i 
        heap = []
        for i, v in enumerate(arr):
            heapq.heappush(heap, (-int(v), i))
        for i, v in enumerate(arr):
            heap_v = heap[0][0] * -1
            if int(v) != heap_v:
                index = dict_index[heap_v]
                # print(f'[{v}] == [{heap_v * -1}] | {i} <> {index}')
                arr[i], arr[index] = arr[index], arr[i]
                break
            else:
                heapq.heappop(heap)
        return int(''.join(arr))
            
    
# print(Solution().maximumSwap(2736)) # 7236
# print(Solution().maximumSwap(9973)) # 7236

# 98368 -> 98863
print(Solution().maximumSwap(98368))

# 1993 -> 9913
print(Solution().maximumSwap(1993))