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

int main()
{
    // ABC279D
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll a, b;
    cin >> a >> b;
    ll l = 0, r = a / b;
    auto f = [&](ll x)
    {
        double res = (double)a / sqrt(x + 1) + (double)b * x;
        return res;
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
    double ans = min({f(l), f(l + 1), f(r)});

    cout << fixed << setprecision(10);
    cout << ans << endl;
    return 0;
}