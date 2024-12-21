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
    // ABC167D
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        int a;
        cin >> a;
        a--;
        A[i] = a;
    }

    // 制約より、2^60までですべての数を表せる(2^60>10^18より)
    vector<vector<int>> dp(60, vector<int>(N, 0));
    // 穴iから2^0=1日後の移動は、A[i]と一致
    for (int i = 0; i < N; i++)
    {
        dp[0][i] = A[i];
    }
    for (int i = 1; i < 60; i++)
    {
        for (int j = 0; j < N; j++)
        {
            dp[i][j] = dp[i - 1][dp[i - 1][j]];
        }
    }
    // 答えの初期値を現在位置(1(0-indexedで0))にする
    int ans = 0;

    rep(j, 60)
    {
        if (K & (1LL << j)) // Kと1<<jでAND。Kの下からj桁目が2進数表記で1なら、真(非ゼロ)
        {
            ans = dp[j][ans];
        }
    }
    cout << ans + 1 << endl;
    return 0;
}