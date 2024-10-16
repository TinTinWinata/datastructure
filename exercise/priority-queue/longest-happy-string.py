import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a,'a'), (-b, 'b'), (-c, 'c')]
        heap = list(filter(lambda x: x[0] != 0, heap))
        
        heapq.heapify(heap) 
        result = ''
        same_current = []
        def is_still_valid(char):
          return len(same_current) >= 2 and same_current[len(same_current) - 1] == char
        while heap:
            (priority, char) = heapq.heappop(heap)
            if is_still_valid(char) and len(heap) > 0:
              (sec_priority, sec_char) = heapq.heappop(heap)
              result += sec_char
              if sec_priority + 1 != 0:
                heapq.heappush(heap, (sec_priority + 1, sec_char))
              heapq.heappush(heap, (priority, char))  
              same_current = []
            elif is_still_valid(char) and len(heap) == 0:
              break
            else:
              result += char
              if priority + 1 != 0:
                heapq.heappush(heap, (priority + 1, char))
              same_current.append(char)
        return result
    
print(Solution().longestDiverseString(7, 1, 0))