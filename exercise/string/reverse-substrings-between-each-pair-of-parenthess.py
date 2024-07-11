from collections import deque

class Solution(object):
    def reverseParentheses(self, s):
        st = deque()
        for i, v in enumerate(s):
            if v == '(':
                st.append((v, i))
            if v == ')':
                (_, firstI) = st.pop()
                substr = s[i-1:firstI:-1]
                s = s[:firstI+1] + substr + s[i :]
        return s.replace('(', '').replace(')', '')
                
s = Solution()
print(s.reverseParentheses('(abcd)'))
print(s.reverseParentheses("(u(love)i)"))
print(s.reverseParentheses("(ed(et(oc))el)"))
