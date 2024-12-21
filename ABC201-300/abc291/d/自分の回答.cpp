#include <bits/stdc++.h>

using namespace std;
int main()
{
    long long mod = 998244353LL;
    int N;
    cin >> N;
    vector<pair<long long, long long>> dp(N, {0LL, 0LL});
    dp[0] = {1LL, 1LL};
    vector<long long> A(N), B(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i] >> B[i];
    }
    for (int i = 1; i < N; i++)
    {
        if (A[i] != A[i - 1])
        {
            dp[i].first = (dp[i].first + dp[i - 1].first) % mod;
        }
        if (B[i] != A[i - 1])
        {
            dp[i].second = (dp[i].second + dp[i - 1].first) % mod;
        }
        if (A[i] != B[i - 1])
        {
            dp[i].first = (dp[i].first + dp[i - 1].second) % mod;
        }
        if (B[i] != B[i - 1])
        {
            dp[i].second = (dp[i].second + dp[i - 1].second) % mod;
        }
    }
    cout << (dp[N - 1].first + dp[N - 1].second) % mod << endl;
    return 0;
}
