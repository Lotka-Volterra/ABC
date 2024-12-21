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
// ABC211D
// 入力: グラフ G と,探索の始点 s
// 出力: 頂点Nへの経路数
ll BFS(const Graph &G, int s)
{
    int N = (int)G.size();    // 頂点数
    vector<int> dist(N, -1);  // 全頂点を「未訪問」に初期化
    vector<ll> count(N, 0LL); // 全頂点の経路数を初期化
    queue<int> que;

    // 初期条件(頂点1を初期頂点とする)
    dist[s] = 0;
    que.push(s); // 1を訪問予定頂点とする
    count[s] = 1LL;
    // BFS開始(キューが空になるまで探索を行う)
    while (!que.empty())
    {
        int v = que.front(); // キューから先頭頂点を取り出す
        que.pop();

        // vから辿れる頂点をすべて調べる
        for (int x : G[v])
        {
            if (dist[x] == -1) // 未発見の頂点の場合
            {
                // 新たに発見した頂点について距離情報を更新
                dist[x] = dist[v] + 1;
                // 経路数を更新
                count[x] += count[v];
                // キューに追加
                que.push(x);
            }
            else if (dist[x] == dist[v] + 1) // 発見済みの頂点だが最短経路の場合
            {
                // 経路数を更新
                count[x] += count[v];
                count[x] %= MOD;
            }
            // その他の場合（発見済みの頂点かつ最短経路でない場合）は何も行わない
        }
    }
    return count[N - 1];
}

int main()
{
    // 頂点数と変数
    int N, M;
    cin >> N >> M;
    // グラフ入力受取(ここでは無向グラフを想定)
    // 注意 ここでは1-indexedに補正している
    Graph G(N + 1);
    for (int i = 1; i < M + 1; i++)
    {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    // 結果出力(頂点1から頂点Nへの経路数を見る)
    cout << BFS(G, 1) << endl;
    return 0;
}