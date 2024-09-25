from typing import List

class Node :
    def __init__(self, val, word = ''):
        self.val = val
        self.childs = {}
        self.word = word
        self.terminal = False
    
class Trie:

    def __init__(self):
        self.root = Node('\0')

    def insert(self, word: str) -> None:
        cursor = self.root
        for v in word:
            if v not in cursor.childs:
                cursor.childs[v] = Node(v)
            cursor = cursor.childs[v]
        cursor.terminal = True
        cursor.word = word

    def dfs(self, root: Node, arr: List[str]):
        if root.terminal:
            arr.append(root.word)
        if len(arr) >= 3:
            return
        for v in  sorted(root.childs.keys()):
          self.dfs(root.childs[v], arr)

    def search(self, word: str) -> List[str]:
        cursor = self.root
        results = []
        for v in word:
            if v not in cursor.childs:
                while len(results)< len(word):
                    results.append([])
                break
            arr = []
            cursor = cursor.childs[v]
            self.dfs(cursor, arr)
            results.append(arr[:3])

        while len(results) < len(word):
            results.append([])
        
        return results 
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for v in sorted(products):
            trie.insert(v)
        return trie.search(searchWord)
        
# print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
