from typing import List, Set

class Node:
    def __init__(self, var, val, undir):
        self.val = val
        self.var = var
        self.undir = undir

class Solution:
    def addGraphs(self, a, b, v):
        new_node_a = Node(b, v, False)
        new_node_b = Node(a, v, True)
        if a not in self.graphs:
            self.graphs[a] = [new_node_a]
        else:
            self.graphs[a].append(new_node_a)
        if b not in self.graphs:
            self.graphs[b] = [new_node_b]
        else:
            self.graphs[b].append(new_node_b)
    
    def dfs(self, current: str, target: str, current_value: float, visited: Set[int]) -> float:
        if current in visited or current not in self.graphs:
            return -1
        visited.add(current)
        for node in self.graphs[current]:
            if node.var in visited:
                continue
            new_current_value = 0
            if not node.undir:
                new_current_value = current_value * node.val
            else:
                new_current_value = current_value * (1 / node.val)
            if node.var == target:
                return new_current_value
            res = self.dfs(node.var, target, new_current_value, visited)
            if res != -1:
                return res
        return -1
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graphs = {}
        for i, arr in enumerate(equations):
            a = arr[0]
            b = arr[1]
            v = values[i]
            self.addGraphs(a, b, v)
        results = []
        for q in queries:
            a = q[0]
            b = q[1]
            if a in self.graphs and b in self.graphs and a == b:
                results.append(1)
            else:
                results.append(self.dfs(a, b, 1, set()))
        return results

# print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
# print(Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x2","x4"]]))