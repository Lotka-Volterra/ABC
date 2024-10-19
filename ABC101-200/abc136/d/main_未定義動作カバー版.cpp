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
    string S;
    cin >> S;
    vector<int> L;
    vector<int> R;
    int N = (int)S.size();
    rep(i, N)
    {
        if (S[i] == 'R' && S[i + 1] == 'L')
        {
            R.push_back(i);
            L.push_back(i + 1);
        }
    }
    vector<int> ans(N, 0);
    rep(i, N)
    {
        if (S[i] == 'R')
        {
            int r = *lower_bound(R.begin(), R.end(), i);
            if ((r - i) % 2 == 0)
            {
                ans[r]++;
            }
            else
            {
                ans[r + 1]++;
            }
        }
        else
        {
            auto l = lower_bound(L.begin(), L.end(), i);
            if (l != L.end() && *l == i)
            {
                ans[*l]++;
            }
            else
            {
                if (l == L.end())
                {
                    int lindex = L[L.size() - 1];
                    if ((i - lindex) % 2 == 0)
                    {
                        ans[lindex]++;
                    }
                    else
                    {
                        ans[lindex - 1]++;
                    }
                }
                else
                {
                    l--;
                    if ((i - *l) % 2 == 0)
                    {
                        ans[*l]++;
                    }
                    else
                    {
                        ans[*l - 1]++;
                    }
                }
            }
        }
    }
    rep(i, N)
    {
        if (i != 0)
        {
            cout << " ";
        }
        cout << ans[i];
    }
    cout << endl;
    return 0;
}