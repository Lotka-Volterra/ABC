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
// ABC270C
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
    int N, M;
    cin >> N >> M;
    if (M == 0)
    {
        cout << 1 << endl;
        return 0;
    }
    // 左端として0,右端としてN+1に青いスタンプが押されているとする
    vector<ll> A(M + 2, 0);
    A[M + 1] = N + 1;
    for (int i = 1; i <= M + 1; i++)
    {
        cin >> A[i];
    }
    sort(A.begin(), A.end());

    vector<ll> WidthList;
    ll min_width = N;
    rep(i, M + 1)
    {
        ll width = A[i + 1] - A[i] - 1; // 青いスタンプ間の間隔
        if (width > 0)
        {
            min_width = min(min_width, width);
        }

        WidthList.push_back(width);
    }
    ll ans = 0;
    rep(i, (int)WidthList.size())
    {
        ans += (WidthList[i] + min_width - 1) / min_width;
    }
    cout << ans << endl;
    return 0;
}