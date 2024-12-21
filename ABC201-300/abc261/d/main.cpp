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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    vector<ll> X(N);
    rep(i, N)
    {
        cin >> X[i];
    }
    map<int, ll> money;
    rep(i, M)
    {
        int c;
        ll y;
        cin >> c >> y;
        money[c] = y;
    }
    vector dp(N + 1, vector<ll>(N + 1, -1));
    dp[0][0] = 0;
    rep(i, N)
    {
        rep(j, N)
        {
            if (dp[i][j] >= 0)
            {
                ll bonus = 0;
                if (money.find(j + 1) != money.end())
                {
                    bonus = money[j + 1];
                }

                dp[i + 1][j + 1] = dp[i][j] + X[i] + bonus;
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j]);
            }
        }
    }
    ll ans = 0;
    rep(i, N + 1)
    {
        ans = max(ans, dp[N][i]);
    }
    cout << ans << endl;
    return 0;
}