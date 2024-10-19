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
    vector<ll> A(N);
    rep(i, N)
    {
        cin >> A[i];
    }
    vector<ll> B(N);
    rep(i, N)
    {
        cin >> B[i];
    }
    vector<vector<ll>> C(N, vector<ll>(3001, 0));
    for (int i = 0; i < 3001; i++)
    {
        if (A[0] <= i && i <= B[0])
        {
            C[0][i] = 1;
        }
    }
    for (int i = 0; i < N - 1; i++)
    {
        ll sum = 0;
        for (ll j = min(A[i + 1], A[i]); j <= B[i + 1]; j++)
        {
            sum += C[i][j];
            sum %= 998244353;
        }

        for (ll j = B[i + 1]; j >= A[i + 1]; --j)
        {
            C[i + 1][j] += sum;
            C[i + 1][j] %= 998244353;
            sum -= C[i][j];
            if (sum < 0)
            {
                sum += 998244353;
            }
        }
    }

    ll ans = 0;
    for (int i = 0; i < 3001; i++)
    {
        ans += C[N - 1][i];
        ans %= 998244353;
    }
    cout << ans << endl;
    return 0;
}