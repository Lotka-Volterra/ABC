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
    ll A, B;
    cin >> N >> A >> B;
    vector<char> S(2 * N + 1);
    for (int i = 1; i < N + 1; i++)
    {
        char c;
        cin >> c;
        S[i] = c;
        S[i + N] = c;
    }
    ll ans = pow(10, 13);
    // ずらすのは、0文字からN-1文字まで
    rep(zurasu, N)
    {
        ll count = 0;
        for (int i = 1; i < (N + 1) / 2 + 1; i++)
        {

            if (S[i + zurasu] != S[N + 1 + zurasu - i])
            {
                count++;
            }
        }
        ll temp = 0;
        temp += count * B;
        temp += A * (ll)zurasu;
        ans = min(ans, temp);
    }
    cout << ans << endl;
    return 0;
}