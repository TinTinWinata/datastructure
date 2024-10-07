class Solution:
    def minLength(self, s: str) -> int:
        st = []
        dict = {
            'B' : 'A',
            'D' : 'C'
        }
        for v in s:
            is_pop = False
            if st: 
                last_v = st[len(st) - 1]
                if v in dict and dict[v] == last_v:
                    st.pop()
                    is_pop = True
            if not is_pop:
              st.append(v)
        return len(st)
    
print(Solution().minLength("ABFCACDB"))
print(Solution().minLength("ACBBD"))