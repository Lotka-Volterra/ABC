#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using Graph = vector<vector<int>>;
// using namespace atcoder;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
// usage:rep(i,3){ processing }  i starts at 0 and increments by 1 until it reaches n.
#define rep1(i, n) for (int i = 1; i < (int)(n); ++i)
// usage:rep(i,3){ processing }  i starts at 1 and increments by 1 until it reaches n.
#define rep2(i, s, n) for (int i = (s); i < (int)(n); ++i)
// usage:rep2(i,1,3){ processing }  i starts at s and increments by 1 until it reaches n.
#define Yes cout << "Yes" << endl
#define No cout << "No" << endl
#define YES cout << "YES" << endl
#define NO cout << "NO" << endl
// 無限大を表す値
const ll INF = 1LL << 60; // 十分大きな値を用いる(ここでは2^60)
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
vector<int> input(int N)
{
    vector<int> vec(N);
    for (int i = 0; i < N; ++i)
    {
        cin >> vec.at(i);
    }
    return vec;
}
// aの階乗a!を返す
ll factorial(ll a)
{
    ll ans = 1;
    rep1(i, a + 1)
    {
        ans *= i;
    }
    return ans;
}
// aの階乗a!をmで割った余りを返す
ll factorial_mod(ll a, ll m)
{
    ll ans = 1;
    rep1(i, a + 1)
    {
        ans = ans * i % m;
    }
    return ans;
}
// a**bをmで割った余りを返す
ll power_mod(ll a, ll b, ll m)
{
    // pはa**1,a**2,a**4と変化
    ll p = a, ans = 1LL;
    // bは10**9以下とする。そのため、iは2**30>10**9まで
    // しっくりこなかったら鉄則本A29の実装にする
    rep(i, 30)
    {
        if (b == 0)
        {
            break;
        }
        if (b % 2 == 1)
        {
            ans = ans * p % m;
        }
        p = p * p % m;
        b /= 2;
    }
    return ans;
}
// arithmetic progression 等差数列
// 1からxまでの和を返す
ll arith(ll x) { return x * (x + 1) / 2; }
// なお、aからa*nまで、aのn個の倍数の和は、a*arith(n)で求められる。(初項=公差=aの等差数列の和)
// 初項 a 公差 d 項数 n の等差数列の和を返す
ll arith(ll a, ll d, ll n)
{
    return n * (2 * a + (n - 1) * d) / 2;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, X;
    cin >> N >> X;
    vector<int> A(N), B(N);
    rep(i, N)
    {
        cin >> A[i] >> B[i];
    }
    vector dp(N + 1, vector<bool>(X + 1, false));
    dp[0][0] = true;
    rep(i, N)
    {
        rep(j, X + 1)
        {
            if (!dp[i][j])
            {
                continue;
            }
            rep(k, B[i] + 1)
            {
                if (A[i] * k + j > X)
                {
                    break;
                }
                dp[i + 1][A[i] * k + j] = true;
            }
        }
    }
    if (dp[N][X])
    {
        Yes;
    }
    else
    {
        No;
    }

    return 0;
}