#include <bits/stdc++.h>

using namespace std;
// using namespace atcoder;
using ll = long long;
using Graph = vector<vector<int>>;
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
// 入力: グラフ G と,探索の始点 s
// 出力: s から各頂点への最短経路長を表す配列
vector<int> BFS(const Graph &G, int s)
{
    int N = (int)G.size();   // 頂点数
    vector<int> dist(N, -1); // 全頂点を「未訪問」に初期化
    queue<int> que;

    // 初期条件(頂点0を初期頂点とする)
    dist[s] = 0;
    que.push(s); // 0を訪問予定頂点とする

    // BFS開始(キューが空になるまで探索を行う)
    while (!que.empty())
    {
        int v = que.front(); // キューから先頭頂点を取り出す
        que.pop();

        // vから辿れる頂点をすべて調べる
        for (int x : G[v])
        {
            // すでに発見済みの頂点は探索しない
            if (dist[x] != -1)
            {
                continue;
            }
            // 新たに発見した頂点について距離情報を更新してキューに追加
            dist[x] = dist[v] + 1;
            que.push(x);
        }
    }
    return dist;
}
int main()
{
    // 頂点数と変数
    ll N;
    cin >> N;
    vector<ll> A(N);
    rep(i, N)
    {
        cin >> A[i];
    }
    map<ll, ll> M;
    rep(i, N)
    {
        if (M.find(A[i]) != M.end())
        {
            M[A[i]]++;
        }
        else
        {
            M[A[i]] = 1;
        }
    }

    ll ans = 0LL;
    for (auto i = M.begin(); i != M.end(); ++i)
    {
        ll j = i->second;
        ans += j * (j - 1) / 2;
    }
    rep(i, N)
    {
        cout << ans - (M[A[i]] - 1) << endl;
    }
    return 0;
}