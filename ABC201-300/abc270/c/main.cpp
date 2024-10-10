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
// パスを出力する用のDFS
deque<int> deq; // 両端キュー double-ended queue.パスの出力用
bool stop;      // 目的地 to に到達したかどうか
void dfsRoute(const Graph &G, int v, int to)
{
    if (!stop)
    {
        deq.push_back(v);
    }
    seen[v] = true;
    if (v == to)
    {
        stop = true;
    }
    for (auto next_v : G[v])
    {
        if (seen[next_v])
        {
            continue; // next_vが探索済みなら探索しない
        }
        dfsRoute(G, next_v, to); // 再帰的に探索
    }
    // toに最終的に到達しなかった場合はdeqから頂点を除く
    if (!stop)
    {
        deq.pop_back();
    }
    return;
}
int main()
{
    // Nが頂点数、Mが次数
    int N, x, y;
    cin >> N >> x >> y;
    // グラフ入力受取（無向グラフを想定）
    Graph G(N + 1);
    rep(i, N - 1)
    {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    // 探索
    // 注意！下記ではN+1で初期化しているが、これは1-indexedな頂点に補正している
    seen.assign(N + 1, false); // 初期状態では全頂点が未訪問(false)
    stop = false;
    dfsRoute(G, x, y);
    while (!deq.empty())
    {
        cout << deq.front();
        deq.pop_front();
        if (deq.empty())
        {
            cout << endl;
        }
        else
        {
            cout << " ";
        }
    }
    return 0;
}