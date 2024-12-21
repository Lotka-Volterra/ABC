#include <bits/stdc++.h>
// #include <atcoder/all>

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

ll solve1(ll N, ll M)
{
    if (N * N < M)
    {
        return -1;
    }
    ll ans = 1LL << 60;

    for (ll a = 1LL; a * a <= M; a++)
    {
        if (a > N)
        {
            break;
        }
        ll b = (M + a - 1LL) / a;
        if (M % a == 0 && b <= N)
        {
            return M;
        }
        else if (M % a != 0 && b <= N)
        {
            ans = min(ans, a * b);
        }
    }
    return ans;
}

ll solve2(ll n, ll m)
{
    ll INF = 2e+18;
    ll ans = INF;
    for (long long i = 1; i <= n; i++)
    {
        ll x = (m + i - 1) / i;
        if (x <= n)
            ans = min(ans, i * x);
        if (i > x)
            break;
    }
    if (ans == INF)
        return -1;
    else
        return ans;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // ll N = 123456789123, M = 987654321987;
    ll M = 987654321987;

    for (ll n = 1; n <= 1e12; n++)
    {

        if (n % 10000000000LL == 0)
        {
            cout << n << "回" << endl;
        }

        if (solve1(n, M) != solve2(n, M))
        {
            cout << n << " " << M << endl;
        }
    }
    return 0;
}