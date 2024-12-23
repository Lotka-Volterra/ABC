#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
// usage:rep(i,3){ processing }  i starts at 0 and increments by 1 until it reaches n.
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
// usage:rep2(i,1,3){ processing }  i starts at s and increments by 1 until it reaches n.
#define Yes cout << "Yes" << endl
#define No cout << "No" << endl
#define YES cout << "YES" << endl
#define NO cout << "NO" << endl
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

// Union-Find けんちょん本
// このコードは0-indexedの前提。1-indexedを0-indexedにするには、引数のx,yを修正すること
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
    // UnionFind定義時は、引数に十分大きな値を渡すこと
    int N;
    cin >> N;
    UnionFind uf(2 * N);
    map<string, int> dict;
    rep(i, N)
    {
        string s, t;
        cin >> s >> t;
        if (dict.find(s) == dict.end())
        {
            dict[s] = 2 * i + 1;
        }
        if (dict.find(t) == dict.end())
        {
            dict[t] = 2 * (i + 1);
        }
        if (uf.is_same(dict[s], dict[t]))
        {
            cout << "No" << endl;
            return 0;
        }

        uf.unite(dict[s], dict[t]);
    }
    cout << "Yes" << endl;
    return 0;
}