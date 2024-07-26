import heapq

class Graph:
  def __init__(self, n):
    self.nodes = [[] for _ in range(n)]
    self.n = n

  def addEdge(self, a: int, b: int, wt: int, undir: bool = True):
    self.nodes[a].append((wt, b))
    if undir:
      self.nodes[b].append((wt, a))
  
  def printAll(self):
    for i, node in enumerate(self.nodes):
      print(f'Node - {i} : ', node)
  
  def djikstra(self, src: int, desc: int):
    dist = {i: float('+inf') for i in range(self.n)}
    dist[src] = 0
    pq = [(0, src)]
    while len(pq) != 0:
      currWeight, curr = heapq.heappop(pq)
      for weight, neighbor in self.nodes[curr]:
        distance = weight + currWeight
        if distance < dist[neighbor]:
          dist[neighbor] = distance
          heapq.heappush(pq, (distance, neighbor))
    print('Dist : ', dist)
    return dist[desc]

        

if __name__ == '__main__':
  graph = Graph(6)
  graph.addEdge(0,2,1)
  graph.addEdge(0,1,10)
  graph.addEdge(1,3,1)
  graph.addEdge(2,3,1)
  graph.addEdge(1,4,1)
  graph.addEdge(4,5,10)
  # graph.printAll()
  print('Djikstra Result : ', graph.djikstra(0, 5))