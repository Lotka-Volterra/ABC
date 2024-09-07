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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, x, y;
    cin >> N;
    auto points = vector<pair<int, int>>(N);
    int point[5001][5001];
    rep(i, 5001)
    {
        rep(j, 5001)
        {
            point[i][j] = 0;
        }
    }
    rep(i, N)
    {
        cin >> x >> y;
        point[x][y] = 1;
        points.push_back({x, y});
    }
    int x1, y1, x2, y2, cx, cy, dx, dy, ans = 0;
    rep(i, N - 1)
    {
        for (int j = i + 1; j < N; j++)
        {
            x1 = points[i].first;
            y1 = points[i].second;
            x2 = points[j].first;
            y2 = points[j].second;
            cx = x2 + y2 - y1;
            cy = y2 + x1 - x2;
            dx = x1 + y2 - y1;
            dy = y1 + x1 - x2;
            if (point[cx][cy] == 1 && point[dx][dy] == 1)
            {
                ans = max(ans, (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            }
            cx = x2 + y1 - y2;
            cy = y2 + x2 - x1;
            dx = x1 + y1 - y2;
            dy = y1 + x2 - x1;
            if (point[cx][cy] == 1 && point[dx][dy] == 1)
            {
                ans = max(ans, (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
            }
        }
    }
    cout << ans << endl;
    return 0;
}