class Solution:
    def __init__(self):
        self.n = 1005
        self.father = [0] * self.n
        for i in range(self.n):
            self.father[i] = i

    def find(self, u) -> int:
        if u == self.father[u]:
            return u
        else:
            self.father[u] = self.find(self.father[u])
        return self.father[u]

    def join(self, u, v):
        fa_u, fa_v = self.find(u), self.find(v)
        if fa_u == fa_v:
            return
        self.father[fa_v] = fa_u
        return

    def same(self, u, v) -> bool:
        return self.find(u) == self.find(v)

    def get_remove_edge(self, edges):
        for edge in edges:
            if self.same(edge[0], edge[1]):
                return edge
            else:
                self.join(edge[0], edge[1])
        return []

    def is_tree_after_remove_edge(self, edges, delete_edge_idx, len_edges):
        for i in range(len_edges):
            if i == delete_edge_idx:
                continue
            if self.same(edges[i][0], edges[i][1]):
                return False
            self.join(edges[i][0], edges[i][1])
        return True

    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        len_edges = len(edges)
        in_degrees = [0] * self.n
        for i in range(len_edges):
            in_degrees[edges[i][1]] += 1
        cnt = []
        for i in range(len_edges - 1, -1, -1):
            if in_degrees[edges[i][1]] == 2:
                cnt.append(i)
        if len(cnt) > 0:
            if self.is_tree_after_remove_edge(edges, cnt[0], len_edges):
                return edges[cnt[0]]
            return edges[cnt[1]]
        return self.get_remove_edge(edges)

edges = [[1,2],[1,3],[2,3]]
s = Solution()
print(s.findRedundantDirectedConnection(edges))