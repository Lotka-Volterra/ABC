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
    // 鉄則本A57
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    cin >> N >> Q;
    vector<int> A(N + 1, 0);
    for (int i = 1; i < N + 1; i++)
    {
        cin >> A[i];
    }
    // 制約より、2^29までですべての数を表せる(2^30>10^9より)
    vector<vector<int>> dp(30, vector<int>(N + 1, 0));
    // 穴iから2^0=1日後の移動は、A[i]と一致
    for (int i = 1; i < N + 1; i++)
    {
        dp[0][i] = A[i];
    }
    for (int i = 1; i < 30; i++)
    {
        for (int j = 1; j < N + 1; j++)
        {
            dp[i][j] = dp[i - 1][dp[i - 1][j]];
        }
    }

    rep(i, Q)
    {
        ll x, y;
        cin >> x >> y;
        // 答えの初期値を現在位置(x)にする
        int ans = x;
        rep(j, 30)
        {
            if (y & (1 << j)) // yと1<<jでAND。yの下からj桁目が2進数表記で1なら、真(非ゼロ)
            {
                ans = dp[j][ans];
            }
        }
        cout << ans << endl;
    }
    return 0;
}