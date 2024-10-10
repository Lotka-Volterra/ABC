#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
// Union-Find けんちょん本
struct UnionFind
{
    vector<int> par, siz;
    // 初期化
    UnionFind(int n) : par(n, -1), siz(n, 1) {}
    // 根を求める
    int root(int x)
    {
        if (par[x] == -1)
            return x; // xが根の場合はxを返す
        else
            return par[x] = root(par[x]);
    }
    // xとyが同じグループに属するかどうか(根が一致するかどうか)
    bool is_same(int x, int y)
    {
        return root(x) == root(y);
    }
    // xを含むグループとyを含むグループとを併合する
    bool unite(int x, int y)
    {
        // x,yをそれぞれ根まで移動する
        x = root(x);
        y = root(y);
        // すでに同じグループのときは何もしない
        if (x == y)
        {
            return false;
        }
        // union by size (y側のサイズが小さくなるようにする)
        if (siz[x] < siz[y])
        {
            swap(x, y);
        }
        // yをxの子とする
        par[y] = x;
        siz[x] += siz[y];
        return true;
    }
    // xを含むグループのサイズ
    int size(int x)
    {
        return siz[root(x)];
    }
};
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    UnionFind uf(N);
    int ans = 0;
    rep(i, M)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        if (uf.is_same(a, b))
        {
            ans++;
        }
        else
        {
            uf.unite(a, b);
        }
    }
    cout << ans << endl;
    return 0;
}