#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;

int main()
{
    int n;
    ll L, R;
    cin >> n >> L >> R;
    vector<ll> a(n);
    rep(i, n)
    {
        cin >> a[i];
    }
    vector dp(n, vector<ll>(3, 1e18));
    dp[0][0] = L;
    dp[0][1] = a[0];
    dp[0][2] = R;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            dp[i + 1][0] = dp[i][0] + L;                            // Lへの移動はLからだけ
            dp[i + 1][1] = min(dp[i][0], dp[i][1]) + a[i + 1];      // Aへの移動はLかAから
            dp[i + 1][2] = min({dp[i][0], dp[i][1], dp[i][2]}) + R; // Rへの移動はL,A,Rのどれか
        }
    }

    cout << min({dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]}) << endl;
}
