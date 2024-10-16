from collections import deque
from typing import List

def getRecommendedFriends(n: int, friendships: List[List[int]]) -> List[int]:
  graph = [[] for _ in range(n)]
  for u, v in friendships:
    graph[u].append(v)
    graph[v].append(u)
  recommended = []
  for i in range(n):
    # bfs
    max_common = {}
    greatest_max = 0
    greatest_node = -1
    queue = deque([(i, 0)]) # node, steps
    visited = set()
    def add_to_max_common(node):
      nonlocal max_common
      nonlocal greatest_node
      nonlocal greatest_max
      nonlocal i
      if node == i or node in graph[i]:
        return
      if node not in max_common:
        max_common[node] = 0
      max_common[node] += 1
      if max_common[node] == greatest_max:
        if node < greatest_node:
          greatest_node = node
      if max_common[node] > greatest_max:
        greatest_max = max_common[node]
        greatest_node = node
    while queue:
      node, steps = queue.pop()
      visited.add(node)
      if steps == 2:
        add_to_max_common(node)
        continue
      for next_node in graph[node]:
        if next_node not in visited:
          queue.appendleft((next_node, steps + 1))
    recommended.append(greatest_node)
  return recommended

# print(getRecommendedFriends(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]))
# print(getRecommendedFriends(3, [[0, 1], [1, 2], [2, 0]]))
# print(getRecommendedFriends(3, [[0, 1], [0, 2]]))
# print(getRecommendedFriends(4, [[0, 1], [1, 2], [1, 3]]))
# print(getRecommendedFriends(5, [[0, 1], [1, 4], [1, 3], [1, 2]]))
print(getRecommendedFriends(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))