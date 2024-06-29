class Node:
    def __init__(self, v):
        self.v = v
        self.ancs = set()
        self.visited = False

    def addAncs(self, v):
        if v not in self.ancs:
          self.ancs.add(v)

class Graph:
    def __init__(self, n):
        self.map = {}
        for i in range(n):
            self.map[i] = Node(i) 

    def dfs(self, current):
        current = self.map[current]
        if current.visited:
            return current.ancs
        for anc in list(current.ancs):
            current.ancs.update(self.dfs(anc))  
        current.visited = True
        return current.ancs

    def addEdge(self, i, j):
        self.map[j].addAncs(i)

class Solution(object):
    def getAncestors(self, n, edges):
        graph = Graph(n)
        res = []
        for edge in edges:
            graph.addEdge(edge[0], edge[1])

        for i in range(n):
            graph.dfs(i)

        for node in graph.map.values():
            res.append(sorted(list(node.ancs)))
        return res
        
s = Solution()
# print(s.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
# print(s.getAncestors(6, [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]))
print(s.getAncestors(9, [[8,3],[6,3],[1,6],[7,0],[8,5],[2,1],[4,0],[2,3],[0,3],[5,3],[7,4],[4,1]]))