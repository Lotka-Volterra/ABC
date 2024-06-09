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
    int N, F, S;
    cin >> N;
    auto SF = vector<pair<int, int>>(N);
    rep(i, N)
    {
        cin >> F >> S;
        SF[i] = {S, F};
    }
    sort(SF.begin(), SF.end());
    reverse(SF.begin(), SF.end());
    int ans = SF[0].first;
    int flavor = SF[0].second;
    int same = 0, different = 0;
    rep2(i, 1, N)
    {
        if (same != 0 && different != 0)
        {
            break;
        }
        else if (same == 0 && SF[i].second == flavor)
        {
            same = SF[i].first;
        }
        else if (different == 0 && SF[i].second != flavor)
        {
            different = SF[i].first;
        }
    }
    cout << max(ans + same / 2, ans + different) << endl;
    return 0;
}