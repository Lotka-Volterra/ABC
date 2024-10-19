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
int H, W;

// 入力: グラフ G と,探索の始点 x,y
// 出力: s から各頂点への最短経路長を表す配列
vector<vector<int>> BFS(const vector<vector<char>> &G, int x, int y)
{
    vector<vector<int>> dist(H, vector<int>(W, -1)); // 全頂点を「未訪問」に初期化
    queue<pair<int, int>> que;

    // 初期条件(頂点0を初期頂点とする)
    dist[x][y] = 1;
    que.push({x, y}); // 0を訪問予定頂点とする

    // BFS開始(キューが空になるまで探索を行う)
    while (!que.empty())
    {
        auto q = que.front(); // キューから先頭頂点を取り出す
        int cx = q.first,
            cy = q.second;
        que.pop();

        // vから辿れる頂点をすべて調べる
        // 右のマス
        if (cy + 1 < W && G[cx][cy + 1] == '.' && dist[cx][cy + 1] == -1)
        {

            dist[cx][cy + 1] = dist[cx][cy] + 1;
            que.push({cx, cy + 1});
        }
        // 下のマス
        if (cx + 1 < H && G[cx + 1][cy] == '.' && dist[cx + 1][cy] == -1)
        {

            dist[cx + 1][cy] = dist[cx][cy] + 1;
            que.push({cx + 1, cy});
        }
    }
    return dist;
}
int main()
{
    int N;
    cin >> N;
    stack<pair<int, int>> S;
    int sum = 0;
    rep(i, N)
    {
        int a;
        cin >> a;
        if (!S.empty() && S.top().first == a)
        {
            if (S.top().second + 1 >= a)
            {
                sum -= S.top().second;
                S.pop();
            }
            else
            {
                S.top().second += 1;
                sum++;
            }
        }
        else
        {
            S.push({a, 1});
            sum++;
        }
        cout << sum << endl;
    }
    return 0;
}