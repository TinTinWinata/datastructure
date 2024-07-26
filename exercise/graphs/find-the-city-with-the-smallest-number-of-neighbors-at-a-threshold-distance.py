from typing import List
from heapq import heappop, heappush

class Graph:
    def __init__(self, n):
        self.nodes = [[] for _ in range(n)]
        self.n = n
    def addEdge(self, edge):
        self.nodes[edge[0]].append((edge[2], edge[1]))
        self.nodes[edge[1]].append((edge[2], edge[0]))

    def getMinimumDistance(self, maxDistance):
        tempMin = float('+inf')
        temp = None
        for i in range(self.n):
            res = self.djikstra(src=i, maxDistance=maxDistance)
            if res <= tempMin:
                tempMin = res
                temp = i
        return temp
            
    def djikstra(self, src, maxDistance):
        dist = {i: float('+inf') for i in range(self.n)}
        pq = [(0, src)]
        res = set()
        while pq:
            if len(res) == self.n:
                break
            weightCurr, curr = heappop(pq)
            if weightCurr > dist[curr]:
                continue
            for weightNeighbor, neighbor in self.nodes[curr]:
                if neighbor == src:
                    continue
                distance = weightNeighbor + weightCurr
                if distance <= maxDistance and distance < dist[neighbor]:
                    res.add(neighbor)
                    dist[neighbor] = distance
                    heappush(pq, (distance, neighbor))
        return len(res)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = Graph(n)
        for edge in edges:
            graph.addEdge(edge)
        return graph.getMinimumDistance(distanceThreshold)

print(Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
print(Solution().findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
print(Solution().findTheCity(6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], 20))