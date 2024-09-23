from typing import List

key_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
class Solution:
    def dfs(self, digits: str, current: int, result: str):
        if current >= len(digits):
            self.results.append(result)
            return
        for v in key_dict[digits[current]]:
            self.dfs(digits, current + 1, result + v)
        
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.results = []
        self.dfs(digits, 0, "")
        return self.results        
                
                
                
                
                