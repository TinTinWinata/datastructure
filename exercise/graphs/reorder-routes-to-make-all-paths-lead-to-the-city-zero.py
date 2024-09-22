from typing import List, Set
class Solution:
    def dfs(self, graphs: List[List[int]], neighbors: List[List[int]], current, visited: Set[int]):
        if current in visited:
            return
        visited.add(current)
        for v in neighbors[current]:
            if v in visited:
                continue
            if current not in graphs[v]:
                self.result += 1
            self.dfs(graphs, neighbors, v, visited)
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graphs = [set() for _ in range(n)]
        neighbors = [[] for _ in range(n)]
        for v in connections:
            a = v[0]
            b = v[1]
            graphs[a].add(b)
            neighbors[a].append(b)
            neighbors[b].append(a)
        self.result = 0
        self.dfs(graphs, neighbors, 0, set())
        return self.result
        
print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))