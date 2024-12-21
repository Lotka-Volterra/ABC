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
// const ll MOD = 1000000007LL;
const ll MOD = 998244353LL;

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
    vector<ll> A(N);
    rep(i, N)
    {
        cin >> A[i];
    }
    vector dp(N - 1, vector<ll>(10, 0LL));
    dp[0][(A[0] + A[1]) % 10]++; // A[0]=A[1]=2だと、dp[0][4]=2となる。それを表現するためには代入(=1LL)ではなく加算(++)。
    dp[0][(A[0] * A[1]) % 10]++;
    for (int i = 1; i < N - 1; i++)
    {
        for (ll j = 0; j < 10; j++)
        {
            dp[i][(A[i + 1] + j) % 10] = (dp[i][(A[i + 1] + j) % 10] + dp[i - 1][j]) % MOD;
            dp[i][(A[i + 1] * j) % 10] = (dp[i][(A[i + 1] * j) % 10] + dp[i - 1][j]) % MOD;
        }
    }
    rep(i, 10)
    {
        cout << dp[N - 2][i] << endl;
    }
    return 0;
}