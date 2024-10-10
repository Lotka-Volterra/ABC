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

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
vector<int> input(int N)
{
    vector<int> vec(N);
    for (int i = 0; i < N; i++)
    {
        cin >> vec.at(i);
    }
    return vec;
}

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
// 鉄則本A67
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;

    vector<pair<int, int>> choten; // 辺を結ぶ2頂点を格納
    vector<pair<int, int>> hen;    // 辺の長さと、頂点番号のindexを格納
    rep(i, M)
    {
        // a,bが頂点の番号、cが辺の長さ
        int a, b, c;
        cin >> a >> b >> c;
        choten.push_back({a, b});
        hen.push_back({c, i});
    }
    // 辺の長さが短い順でソート(最小全域木だから)
    sort(hen.begin(), hen.end());
    UnionFind uf(N + 1);
    int henCount = 0; // 張った辺の数のカウント
    ll ans = 0LL;     // 最小全域木の辺の長さ
    rep(i, M)
    {
        // 辺数=頂点数-1になったらすべての頂点がつながったことになる
        if (henCount == N - 1)
        {
            break;
        }
        int p = hen[i].second;
        int a = choten[p].first;
        int b = choten[p].second;
        // 2頂点が連結していなければ、連結する
        if (!uf.is_same(a, b))
        {
            uf.unite(a, b);
            henCount++;
            ans += hen[i].first;
        }
    }
    cout << ans << endl;
    return 0;
}