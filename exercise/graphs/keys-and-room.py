from typing import List, Set

class Solution:
    def dfs(self, rooms: List[List[int]], current: int, visited: Set[int]):
        if current in visited:
            return
        keys = rooms[current]
        visited.add(current)
        for v in keys:
            self.dfs(rooms, v, visited)
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
        