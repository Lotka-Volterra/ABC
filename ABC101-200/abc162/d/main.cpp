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
    ll n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> R, G, B;
    set<int> Bs;
    rep(i, n)
    {
        if (s[i] == 'R')
        {
            R.push_back(i);
        }
        else if (s[i] == 'G')
        {
            G.push_back(i);
        }
        else
        {
            B.push_back(i);
            Bs.insert(i);
        }
    }
    ll ans = 0LL;
    for (int r = 0; r < (int)R.size(); r++)
    {
        for (int g = 0; g < (int)G.size(); g++)
        {

            ans += B.size();
            // Bが最小
            if (Bs.find(min(R[r], G[g]) - abs(R[r] - G[g])) != Bs.end())
            {
                ans--;
            }
            // Bが真ん中
            if ((R[r] + G[g]) % 2 == 0 && Bs.find((R[r] + G[g]) / 2) != Bs.end())
            {
                ans--;
            }
            // Bが最大
            if (Bs.find(max(R[r], G[g]) + abs(R[r] - G[g])) != Bs.end())
            {
                ans--;
            }
        }
    }

    cout << ans << endl;
    return 0;
}