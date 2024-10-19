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
    map<ll, ll> M;
    vector<ll> AB;
    for (ll a = 1; a < N; a++)
    {
        for (ll b = 1; b < N; b++)
        {
            if (a * b >= N)
            {
                break;
            }
            AB.push_back(a * b);
            if (M.find(a * b) == M.end())
            {
                M[a * b] = 1;
            }
            else
            {
                M[a * b]++;
            }
        }
    }
    ll ans = 0;
    for (ll ab : AB)
    {
        ll cd = N - ab;
        if (M.find(cd) != M.end())
        {
            ans += M[cd];
        }
    }
    cout << ans << endl;
    return 0;
}