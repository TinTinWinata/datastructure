from typing import List, Dict

class Solution:
    def checkMinimalCost(self, dict: Dict):
        for key in dict:  
          visited = set()
          self.getMinimalCost(key, dict, visited)

    def getMinimalCost(self, curr: int, dict: Dict, visited: set):
        if curr not in dict:
            return {}
        currDict = dict[curr]
        if curr in visited:
            return currDict
        visited.add(curr)
        for key in currDict.copy(): 
              newDict = self.getMinimalCost(key, dict, visited)
              for newKey in newDict:
                  totalCost =newDict[newKey] + currDict[key]
                  if (newKey not in currDict) or (newKey in currDict and totalCost < currDict[newKey]):
                      currDict[newKey] = totalCost
        return currDict
        
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dict = {}
        for i in range(len(original)):
            if original[i] not in dict:
              dict[original[i]] = {}
            
            dict[original[i]][changed[i]] = min(cost[i], dict[original[i]].get(changed[i], float('+inf')))
        self.checkMinimalCost(dict)
        totalCost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                if source[i] in dict and target[i] in dict[source[i]]:
                  totalCost += dict[source[i]][target[i]]
                else:
                  totalCost = -1
                  break
        return totalCost
        

# print(Solution().minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))
# print(Solution().minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1,2]))
# print(Solution().minimumCost("abcd", "abce", ["a"], ["e"], [10000]))
# print(Solution().minimumCost("aaaabadaaa", "dbdadddbad", ["c","a","c","a","a","b","b","b","d","d","c"], ["a","c","b","d","b","c","a","d","c","b","d"], [7,8,11,9,7,6,4,6,9,5,9]))
print(Solution().minimumCost("aaadbdcdac", "cdbabaddba", ["a","c","b","d","b","a","c"], ["c","a","d","b","c","b","d"], [7,2,1,3,6,1,7]))

"aaadbdcdac"
"cdbabaddba"
["a","c","b","d","b","a","c"]
["c","a","d","b","c","b","d"]
[7,   2,  1,  3,  6,  1,  7]