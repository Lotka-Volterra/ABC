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

// ダイクストラ法 ヒープで改良ver けんちょん本より (MlogN)
// 未確定頂点の中で暫定的な最短距離が最小の頂点を探す箇所を改良
// 無限大を表す値
const ll INF = 1LL << 60; // 十分大きな値を用いる(ここでは2^60)
// 辺を表す型 ここでは重みを表す型をlong long型とする
struct Edge
{
    int to;                                             // 隣接頂点番号
    ll weight;                                          // 重み
    Edge(int to, ll weight) : to(to), weight(weight) {} // 隣接頂点と重みの初期化
};
// 重みつきグラフを表す型。辺に重みの情報がある
using Graph = vector<vector<Edge>>;
// 緩和を実施する関数
template <class T>    // 型テンプレート
bool chmin(T &a, T b) // &は参照
{
    if (a > b) // aがbより大きいときはaを最小値bに更新
    {
        a = b;
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // 頂点数,辺数,始点
    int N, M, s;
    cin >> N >> M >> s;
    // 無向グラフ 1-indexedの想定
    Graph G(N + 1);
    for (int i = 0; i < M; i++)
    {
        // aからbへ重みwの辺が張っている
        int a, b, w;
        cin >> a >> b >> w;
        G[a].push_back(Edge(b, w));
        G[b].push_back(Edge(a, w));
    }
    // 距離をINFで初期化
    vector<ll> dist(N + 1, INF);
    // 始点の距離は0
    dist[s] = 0;
    // ダイクストラ法の改良箇所
    // 距離dist[v],頂点番号vのペアを要素とした優先度付きキューを作る
    // 優先度付きキューはデフォルトでは最大値を取得するので、最小値を取得するように変更
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> que;
    que.push(make_pair(dist[s], s)); // 始点の距離0と頂点番号sのペアをキューに追加
    // 頂点が使用済みかどうか管理
    vector<bool> used(N + 1, false);

    while (!que.empty())
    {
        // 使用済みでない頂点のうち,dist値が最小の頂点を探す
        // v: 使用済みでない頂点のうち、d[v]が最小の頂点
        // d: vに対するキー値
        int v = que.top().second;
        ll d = que.top().first;
        // キューから除く。今回の実装では、キューの中の要素のキーを更新せず、1回除去してからキーを更新して再挿入する
        que.pop();
        // d>dist[v]は、vがすでに確定済みの頂点であることを意味する。その場合(d,v)はゴミなのでキューに再挿入しない
        // キューから取り出されるのは、最新かつ最小のデータだけなので、暫定的な最短距離が古いデータはゴミとして残る実装となる
        if (d > dist[v])
        {
            continue;
        }

        // vを始点とした各辺を緩和する
        for (auto e : G[v])
        {
            // toへの暫定的な最短距離と、vからtoへの距離を比較してtoへの最短距離を更新
            if (chmin(dist[e.to], dist[v] + e.weight))
            {
                // 更新があるならキューに挿入
                que.push(make_pair(dist[e.to], e.to));
            }
        }
    }
    // 結果出力
    for (int v = 1; v < N + 1; v++)
    {
        if (dist[v] < INF)
        {
            cout << dist[v] << endl;
        }
        else
        {
            cout << "INF" << endl; // 最短経路が見つからなかった場合
        }
    }

    return 0;
}