#include <bits/stdc++.h>

using namespace std;
using Graph = vector<vector<int>>;
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
// 深さ優先探索
vector<bool> seen;
void dfs(const Graph &G, int v)
{
    seen[v] = true;
    for (auto next_v : G[v])
    {
        if (seen[next_v])
        {
            continue; // next_vが探索済みなら探索しない
        }
        dfs(G, next_v); // 再帰的に探索
    }
}

int main()
{
    // Nが頂点数、Mが次数
    int N, M;
    cin >> N >> M;
    // グラフ入力受取（無向グラフを想定）
    Graph G(N + 1);
    rep(i, M)
    {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    // 探索
    // 注意！下記ではN+1で初期化しているが、これは1-indexedな頂点に補正している
    seen.assign(N + 1, false); // 初期状態では全頂点が未訪問(false)
    // 連結かどうかを調べるには、適当な頂点からDFSを初めて、探索修了後すべての頂点が訪問済みか調べれば良い
    dfs(G, 1);
    for (int i = 1; i < N + 1; i++)
    {
        if (!seen[i])
        {
            cout << "非連結" << endl;
            return 0;
        }
    }
    cout << "連結" << endl;

    // 下記では全頂点からDFSをしている
    // rep(v, N)
    // {
    //     if (seen[v])
    //     {
    //         continue;
    //     }
    //     dfs(G, v); // すでに訪問済みなら探索しない
    // }
    return 0;
}