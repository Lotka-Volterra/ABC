#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using Graph = vector<vector<int>>;

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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n + 1);
    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    seen.assign(n + 1, false); // 初期状態では全頂点が未訪問(false)
    // 連結かどうかを調べるには、適当な頂点からDFSを初めて、探索修了後すべての頂点が訪問済みか調べれば良い
    dfs(graph, 1);
    for (int i = 1; i < n + 1; i++)
    {
        if (!seen[i])
        {
            cout << "No" << endl;
            return 0;
        }
    }
    int one_count = 0, two_count = 0;
    for (int i = 1; i < n + 1; i++)
    {
        int s = graph[i].size();
        if (s == 1)
        {
            one_count++;
        }
        else if (s == 2)
        {
            two_count++;
        }
    }
    // 模範解答は辺の数がN-1本、次数が2以下、グラフが連結で解いている
    // 自分は次数が2の頂点がn-2個かつ次数1の頂点が2個、グラフが連結で解いている
    if (one_count == 2 && two_count == n - 2)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }

    return 0;
}