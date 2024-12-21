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
    int s;
    cin >> s;
    vector dp((s + 2) / 3 + 1, vector<ll>(s + 1, 0));
    for (int i = 3; i <= s; i++)
    {
        dp[1][i] = 1LL;
    }
    for (int i = 1; i < (int)dp.size() - 1; i++)
    {
        for (int j = 3 * i; j < s; j++)
        {
            if (j + 3 <= s)
            {
                dp[i + 1][j + 3] += dp[i][j];
                dp[i + 1][j + 3] %= MOD;
            }
        }
        // 累積和
        for (int j = 1; j < s + 1; j++)
        {
            dp[i + 1][j] = dp[i + 1][j - 1] + dp[i + 1][j];
        }
    }
    ll ans = 0LL;
    rep(i, (int)dp.size())
    {
        ans += dp[i][s];
        ans %= MOD;
    }
    cout << ans << endl;
    return 0;
}