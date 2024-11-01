class Solution:
    def makeFancyString(self, s: str) -> str:
        st = []
        res = ""
        for v in s:
            if len(st) > 0 and st[-1] != v or len(st) == 0:
                st = [v]
            elif(len(st) == 2) and st[0] == v:
                continue
            else:
                st.append(v)
            res += v
        return res
    
print(Solution().makeFancyString("leeetcode")) # "leetcode"