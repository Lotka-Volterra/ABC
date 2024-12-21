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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N, K;
    cin >> N >> K;
    vector<ll> A(N + 1);
    A[0] = 0LL;
    // A[i]にi番目を入れて、インデックスとAiを合わせる
    for (int i = 1; i < N + 1; i++)
    {
        cin >> A[i];
    }
    vector<ll> ruiseki(N + 1);
    ruiseki[0] = 0LL;
    map<ll, vector<ll>> dict;
    for (int i = 1; i < N + 1; i++)
    {
        ruiseki[i] = ruiseki[i - 1] + A[i];
        dict[ruiseki[i]].push_back(i);
    }

    ll ans = 0;
    for (int i = 1; i <= N; i++)
    {
        if (dict.find(ruiseki[i - 1] + K) != dict.end())
        {
            // vector<ll> d = dict[ruiseki[i - 1] + K];
            auto itr = lower_bound(dict[ruiseki[i - 1] + K].begin(), dict[ruiseki[i - 1] + K].end(), i);
            if (itr != dict[ruiseki[i - 1] + K].end())
            {
                ans += (ll)dict[ruiseki[i - 1] + K].size() - (itr - dict[ruiseki[i - 1] + K].begin());
            }
        }
    }
    cout << ans << endl;
    return 0;
}