from typing import List, Set

class Solution:
    def dfs(self, graphs: List[List[int]], current: int, visited: Set[int]):
        if current in visited:
            return
        visited.add(current)
        for v in graphs[current]:
            self.dfs(graphs, v, visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graphs = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    graphs[i].append(j)
        visited = set()
        provinces = 0
        for i in range(n):
            if i in visited:
                continue
            provinces += 1
            self.dfs(graphs, i, visited)
        return provinces
        