from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.request = deque()
        

    def get_recent(self):
        first = self.request[0]
        count = 0
        for v in self.request:
            if first - v <= 3000:
                count += 1
            else:
                break
        return count
            

    def ping(self, t):
       self.request.appendleft(t)
       return self.get_recent()
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)