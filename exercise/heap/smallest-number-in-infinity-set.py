import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.c = 1
        self.s = set()

    def popSmallest(self) -> int:
        if len(self.heap) <= 0 or self.c < self.heap[0]:
            temp = self.c
            self.c += 1
            return temp 
        if self.heap[0] == self.c:
            self.c += 1
        self.s.remove(self.heap[0])
        return heapq.heappop(self.heap)
        

    def addBack(self, num: int) -> None:
        if num in self.s:
            return
        heapq.heappush(self.heap, num)
        self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)