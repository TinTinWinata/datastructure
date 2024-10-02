class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        count = 1
        while len(self.st) > 0 and price >= self.st[len(self.st) - 1][0]:
            count += self.st.pop()[1]
        self.st.append((price, count))
        return count
    

# [[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]
# [1,1,3,4,5,6,7,8,9,10]

# 