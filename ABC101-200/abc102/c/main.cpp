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
    // ABC279D
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<ll> A(N);
    rep(i, N)
    {
        cin >> A[i];
        A[i] -= i;
    }
    sort(A.begin(), A.end());
    ll l = A[0];
    ll r = A[N - 1];
    auto f = [&](ll x)
    {
        ll ans = 0LL;
        rep(i, N)
        {
            ans += abs(A[i] - x);
        }
        return ans;
    };
    while (l + 3 <= r)
    {
        // c1,c2は線分lrを3等分したときの点。左側から、l,c1,c2,rと並ぶ。
        ll c1 = (2 * l + r) / 3;
        ll c2 = (l + 2 * r) / 3;
        if (f(c1) > f(c2))
        {
            l = c1;
        }
        else
        {
            r = c2;
        }
    }
    ll ans = min({f(l), f(l + 1), f(r)});

    cout << ans << endl;
    return 0;
}