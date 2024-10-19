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

    deque<char> deq;
    string S;
    cin >> S;
    rep(i, S.size())
    {
        deq.push_back(S[i]);
    }
    int Q;
    cin >> Q;
    bool reversed = false;
    rep(i, Q)
    {
        int type;
        cin >> type;
        if (type == 1)
        {
            reversed = !reversed;
        }
        else
        {
            int f;
            char c;
            cin >> f >> c;
            if (f == 1)
            {
                if (!reversed)
                {
                    deq.push_front(c);
                }
                else
                {
                    deq.push_back(c);
                }
            }
            else
            {
                if (!reversed)
                {
                    deq.push_back(c);
                }
                else
                {
                    deq.push_front(c);
                }
            }
        }
    }
    vector<char> ans(deq.begin(), deq.end());
    if (!reversed)
    {
        rep(i, ans.size())
        {
            cout << ans[i];
        }
    }
    else
    {
        for (int i = ans.size() - 1; i >= 0; i--)
        {
            cout << ans[i];
        }
    }

    cout << endl;
}