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

// 深さ優先探索
int H, W, K;
map<tuple<int, int, int>, ll> memo;
ll dfs(vector<vector<char>> G, int i, int j, int c, vector<vector<bool>> s)
{

    auto key = make_tuple(i, j, c);
    if (memo.find(key) != memo.end())
    {
        return memo[key];
    }
    if (c == K)
    {
        return 1;
    }
    ll ans = 0;

    s[i][j] = true;
    if (i - 1 >= 0 && G[i - 1][j] != '#' && !s[i - 1][j])
    {
        ans += dfs(G, i - 1, j, c + 1, s);
    }
    if (i + 1 < H && G[i + 1][j] != '#' && !s[i + 1][j])
    {
        ans += dfs(G, i + 1, j, c + 1, s);
    }
    if (j - 1 >= 0 && G[i][j - 1] != '#' && !s[i][j - 1])
    {
        ans += dfs(G, i, j - 1, c + 1, s);
    }
    if (j + 1 < W && G[i][j + 1] != '#' && !s[i][j + 1])
    {
        ans += dfs(G, i, j + 1, c + 1, s);
    }
    // 結果をメモに保存
    memo[key] = ans;
    return ans;
}

int main()
{
    cin >> H >> W >> K;
    vector<vector<char>> HW(H, vector<char>(W, ' '));
    rep(i, H)
    {
        rep(j, W)
        {
            cin >> HW[i][j];
        }
    }
    ll ans = 0;
    vector<vector<bool>> seen(H, vector<bool>(W, false));
    rep(i, H)
    {
        rep(j, W)
        {
            if (HW[i][j] == '#')
            {
                continue;
            }
            ans += dfs(HW, i, j, 0, seen);
        }
    }
    cout << ans << endl;
    return 0;
}