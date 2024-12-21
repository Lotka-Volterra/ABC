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
    ll N, P, Q, R;
    cin >> N >> P >> Q >> R;
    vector<ll> A(N);
    rep(i, N)
    {
        cin >> A[i];
    }
    vector<ll> ruisekiwa(N + 1, 0);
    rep(i, N)
    {
        ruisekiwa[i + 1] = ruisekiwa[i] + A[i];
    }
    for (int x = 0; x < N - 2; x++)
    {
        auto itry = lower_bound(ruisekiwa.begin(), ruisekiwa.end(), ruisekiwa[x] + P);
        if (itry == ruisekiwa.end())
        {
            continue;
        }
        int y = itry - ruisekiwa.begin();
        if (ruisekiwa[y] - ruisekiwa[x] != P)
        {
            continue;
        }
        auto itrz = lower_bound(ruisekiwa.begin(), ruisekiwa.end(), ruisekiwa[y] + Q);
        if (itrz == ruisekiwa.end())
        {
            continue;
        }
        int z = itrz - ruisekiwa.begin();
        if (ruisekiwa[z] - ruisekiwa[y] != Q)
        {
            continue;
        }
        auto itrw = lower_bound(ruisekiwa.begin(), ruisekiwa.end(), ruisekiwa[z] + R);
        if (itrw == ruisekiwa.end())
        {
            continue;
        }
        int w = itrw - ruisekiwa.begin();
        if (ruisekiwa[w] - ruisekiwa[z] != R)
        {
            continue;
        }
        Yes;
        return 0;
    }
    No;
    return 0;
}