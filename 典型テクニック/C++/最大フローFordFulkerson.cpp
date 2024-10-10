#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;

struct Graph
{
    // 辺を表す構造体
    // rev: 逆辺(to, from)がG[to]の中で何番目の要素か
    // cap: 辺(from, to)の容量
    struct Edge
    {
        int rev, from, to, cap;
        Edge(int r, int f, int t, int c) : rev(r), from(f), to(t), cap(c) {}
    };
    // 隣接リスト
    vector<vector<Edge>> list;
    // N: 頂点数
    Graph(int N = 0) : list(N) {}
    // グラフの頂点数取得
    // seenの初期化時にG.size()の取得が必要
    size_t size()
    {
        return list.size();
    }
    // GraphインスタンスをGとして、
    // G.list[v]をG[v]と書けるようにしておく
    vector<Edge> &operator[](int i)
    {
        return list[i];
    }
    // 辺 e = (from, to) の逆辺 (to, from) を取得する
    Edge &redge(const Edge &e)
    {
        return list[e.to][e.rev]; // list[to][eに対応する逆辺のインデックス]
    }
    // 辺 e = (u, v)に流量 f のフローを流す
    // 辺 e = (u, v)の流量が f だけ減少する
    // このとき、逆辺 (v, u) の流量を f だけ増加させる
    void run_flow(Edge &e, int f)
    {
        e.cap -= f;
        redge(e).cap += f;
    }
    // 頂点 from から頂点 to へ容量 cap の辺を張る
    // このとき to から from へも容量 0 の辺を張っておく
    void addEdge(int from, int to, int cap)
    {
        int fromrev = (int)list[from].size();             // 現時点でのlist[from]の要素数(list[from]に逆辺を追加するとき、0-indexedなのでfromrevがちょうど逆辺のインデックスになる)
        int torev = (int)list[to].size();                 // 現時点でのlist[to]の要素数(list[to]に逆辺を追加するとき、0-indexedなのでtorevがちょうど逆辺のインデックスになる)
        list[from].push_back(Edge(torev, from, to, cap)); // 頂点 from から頂点 to へ容量 cap の辺
        list[to].push_back(Edge(fromrev, to, from, 0));   // 頂点 to から from へ容量 0 の辺
    }
};
struct FordFulkerson
{
    static const int INF = 1 << 30; // 無限大を表す値を適切に設定する
    vector<int> seen;

    FordFulkerson() {};

    // 残余グラフ上でs-tパスを見つける(深さ優先探索)
    // 返り値はs-tパス上の容量の最小値(見つからなかったら 0)
    // f: sから vへ到達した過程の各辺の容量の最小値
    int fodfs(Graph &G, int v, int t, int f)
    {
        // 終端 t に到達したらリターン
        if (v == t)
        {
            return f;
        }
        // 深さ優先探索
        seen[v] = true;
        for (auto &e : G[v])
        {
            if (seen[e.to])
            {
                continue;
            }
            // 容量 0 の辺は実際には存在しない
            if (e.cap == 0)
            {
                continue;
            }
            // s-t パスを探す
            // 見つかったら flow はパス上の最小容量
            // 見つからなかったら f = 0
            int flow = fodfs(G, e.to, t, min(f, e.cap));

            // s-tパスが見つからなかったら次の辺を試す
            if (flow == 0)
            {
                continue;
            }

            // s-tパスが見つかった場合の分岐
            // 辺 e に容量 flow のフローを流す
            G.run_flow(e, flow);
            // パス上の最小容量を返す
            return flow;
        }
        // s-tパスが見つからなかったことを表す
        return 0;
    }
    // グラフ G の s-t 間の最大流量を求める
    // ただしリターン時に G は残余グラフになる
    int max_flow(Graph &G, int s, int t)
    {
        int total_flow = 0;
        // 残余グラフに s-t パスがなくなるまで反復
        while (true)
        {
            seen.assign((int)G.size(), 0);
            int flow = fodfs(G, s, t, INF); // 最初はINFを流す。徐々にminで流量が少なくなっていく
            // s-tパスが見つからなかったら終了
            if (flow == 0)
            {
                return total_flow;
            }
            // 答えを加算
            total_flow += flow;
        }
        // no reach
        return 0;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // グラフの頂点
    // N: 頂点数, M: 辺数
    int N, M;
    cin >> N >> M;

    Graph G(N);
    for (int i = 0; i < M; i++)
    {
        int u, v, c;
        // 下記は1-indexedの場合
        // u--; // 1-indexedの頂点番号を0-indexedに変換
        // v--; // 1-indexedの頂点番号を0-indexedに変換
        cin >> u >> v >> c;
        // 容量 c の辺(u, v)を張る
        G.addEdge(u, v, c);
    }
    // Ford Fulkerson法
    FordFulkerson ff;
    int s = 0, t = N - 1; // 0-indexedなので始点が0,終点がN-1
    cout << ff.max_flow(G, s, t) << endl;
    return 0;
}