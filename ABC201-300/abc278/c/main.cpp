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
    map<string, bool> dict;
    int n, q, t, a, b;
    cin >> n >> q;

    rep(i, q)
    {
        cin >> t >> a >> b;
        string ab = to_string(a) + "_" + to_string(b);
        string ba = to_string(b) + "_" + to_string(a);
        // cout << ab << endl;
        // cout << ba << endl;
        if (t == 1)
        {
            dict[ab] = true;
        }
        else if (t == 2)
        {
            dict[ab] = false;
        }
        else
        {
            // cout << dict.count(ab) << endl;
            // cout << dict.count(ba) << endl;
            if (dict.count(ab) && dict.count(ba) && dict[ab] && dict[ba])
            {
                Yes;
            }
            else
            {
                No;
            }
        }
    }

    return 0;
}