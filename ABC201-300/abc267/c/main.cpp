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
    ll N, M;
    cin >> N >> M;
    vector<ll> ruisekiwa(N + 1, 0);
    vector<ll> A(N + 1, 0);
    for (int i = 1; i < N + 1; i++)
    {
        cin >> A[i];
    }
    for (int i = 1; i < N + 1; ++i)
    {
        ruisekiwa[i] = ruisekiwa[i - 1] + A[i];
    }
    ll ans = 0;
    for (ll i = 1; i <= M; i++)
    {
        ans += A[i] * i;
    }
    ll former = ans;
    for (int i = 2; i <= N - M + 1; ++i)
    {
        // cout << ans << endl;
        ll temp = former - (ruisekiwa[i + M - 2] - ruisekiwa[i - 2]) + A[i + M - 1] * M;
        former = temp;
        ans = max(temp, ans);
    }
    cout << ans << endl;
    return 0;
}