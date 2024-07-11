class UnionFind:
    def __init__(self, size):
        # Initialize the parent and rank arrays
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        print('Created : ', self.parent)

    def find(self, p):
        # Path compression heuristic
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        # Union by rank heuristic
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        # Check if p and q have the same root
        return self.find(p) == self.find(q)

# Example usage
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)

print(uf.connected(1, 3))  # True
print(uf.connected(1, 4))  # False
print(uf.connected(4, 5))  # True

# Find operation example
print(uf.find(1))  # Outputs the root of element 1
print(uf.find(5))  # Outputs the root of element 5
