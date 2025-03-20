class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weight = [-1] * n 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, edge_weight):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            self.weight[rootX] &= edge_weight
            return
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.weight[rootX] &= self.weight[rootY] & edge_weight
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            self.weight[rootY] &= self.weight[rootX] & edge_weight
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
            self.weight[rootX] &= self.weight[rootY] & edge_weight

class Solution:
    def minimumCost(self, n, edges, queries):
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)
        result = []
        for s, t in queries:
            if s == t:
                result.append(0)
            elif uf.find(s) == uf.find(t):
                result.append(uf.weight[uf.find(s)])
            else:
                result.append(-1)
        return result
