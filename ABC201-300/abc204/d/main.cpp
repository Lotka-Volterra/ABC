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
    int N;
    cin >> N;
    vector<vector<pair<int, int>>> dp(N + 1, vector<pair<int, int>>(100010, {200010, 200010}));
    dp[0][0] = {0, 0};
    rep(i, N)
    {
        int T;
        cin >> T;
        rep(j, 1000 * N + 1)
        {
            if (dp[i][j].first == 200010 && dp[i][j].second == 200010)
            {
                continue;
            }
            int ovenA = dp[i][j].first;
            int ovenB = dp[i][j].second;
            int Atime = max(ovenA + T, ovenB);
            int Btime = max(ovenB + T, ovenA);
            if (dp[i + 1][Atime].first + dp[i + 1][Atime].second > ovenA + T + ovenB)
            {
                dp[i + 1][Atime] = {ovenA + T, ovenB};
            }
            if (dp[i + 1][Btime].first + dp[i + 1][Btime].second > ovenA + T + ovenB)
            {
                dp[i + 1][Btime] = {ovenA, ovenB + T};
            }
            // dp[i + 1][j + T] = min(dp[i + 1][j + T], +T);
            // dp[i + 1][dp[i][j] + T] = min(dp[i + 1][dp[i][j] + T], j);
        }
        // for (int j = 0; j < 20; j++)
        // {
        //     cout << " " << dp[i + 1][j];
        // }
        // cout << endl;
    }

    int ans = max(dp[N][0].first, dp[N][0].second);
    for (int i = 1; i < dp[N].size(); ++i)
    {
        if (dp[N][i].first == 200010 && dp[N][i].second == 200010)
        {
            continue;
        }

        ans = min(ans, max(dp[N][i].first, dp[N][i].second));
    }
    cout << ans << endl;
    return 0;
}