class Solution:
    def __init__(self):
        self.n = 1005
        self.father = [0] * self.n
        for i in range(self.n):
            self.father[i] = i

    def find(self, u: int):
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])

        return self.father[u]

    def join(self, u: int, v: int):
        fa_u = self.find(u)
        fa_v = self.find(v)
        if fa_u == fa_v:
            return
        self.father[fa_v] = fa_u
        return

    def same(self, u: int, v: int):
        fa_u, fa_v = self.find(u), self.find(v)
        return fa_u == fa_v

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        for edge in edges:
            if self.same(edge[0], edge[1]):
                return edge
            else:
                self.join(edge[0], edge[1])
        return []