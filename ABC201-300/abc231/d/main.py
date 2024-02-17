# Union-Find 木
class unionfind:
    # n 頂点の Union-Find 木を作成
    # （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)  # 最初は親が無い
        self.size = [1] * (n + 1)  # 最初はグループの頂点数が 1

    # 頂点 x の根を返す関数
    def root(self, x):
        # 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素 u, v を統合する関数
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v が異なるグループのときのみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    #  要素 u と v が同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)


# 入力
N, M = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(M)]

conjection = [[] for i in range(N + 1)]
# クエリの処理
uf = unionfind(N)
for u, v in queries:
    # if tp == 1:
    #     uf.unite(u, v)
    # if tp == 2:
    #     if uf.same(u, v):
    #         print("Yes")
    #     else:
    #         print("No")
    # すでに連結であるなら、辺の追加によりループになる
    conjection[u].append(v)
    conjection[v].append(u)
    if uf.same(u, v):
        print("No")
        quit()
    uf.unite(u, v)
    # 辺が3本以上出る
    if len(conjection[u]) >= 3 or len(conjection[v]) >= 3:
        print("No")
        quit()
print("Yes")
