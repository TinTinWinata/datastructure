class Node:
    def __init__(self, v):
        self.val = v
        self.neighbors = []

    def __lt__(self, others):
        return len(self.neighbors) > len(others.neighbors)

class Graph: 
    def __init__(self, n):
        self.lists = [Node(v) for v in range(n)]
        self.map = {}
        for node in self.lists: 
            self.map[node.val] = node

    def addEdge(self, i, j):
        self.lists[i].neighbors.append(j)
        self.lists[j].neighbors.append(i)
    def sort(self):
        self.lists.sort()

class Solution(object):
    def maximumImportance(self, n, roads):
        graph = Graph(n)  
        for road in roads:
            graph.addEdge(road[0], road[1])

        graph.sort()
        total_importances = 0
        
        for i, node in enumerate(graph.lists): 
            importance = n - i 
            total_importances += importance * len(node.neighbors)
        
        return total_importances
        
s = Solution()
print(s.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])) # 43