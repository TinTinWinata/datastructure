class Node :
    def __init__(self, val):
        self.val = val
        self.childs = {}
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

    def search(self, word: str) -> bool:
        cursor = self.root
        for v in word:
            if v not in cursor.childs:
                return False
            cursor = cursor.childs[v] 
        return cursor.terminal
        

    def startsWith(self, prefix: str) -> bool:
        cursor = self.root
        for v in prefix:
            if v not in cursor.childs:
                return False
            cursor = cursor.childs[v] 
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)