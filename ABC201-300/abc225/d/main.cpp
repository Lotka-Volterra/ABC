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
    int N, Q;
    cin >> N >> Q;
    // firstが前の電車、secondが次の電車
    vector<pair<int, int>> train(N + 1);
    rep(i, N + 1)
    {
        train[i] = {i, i};
    }
    rep(i, Q)
    {
        int type;
        cin >> type;
        if (type == 1)
        {
            int x, y;
            cin >> x >> y;
            train[x].second = y;
            train[y].first = x;
        }
        else if (type == 2)
        {
            int x, y;
            cin >> x >> y;
            train[x].second = x;
            train[y].first = y;
        }
        else
        {
            int x;
            cin >> x;
            int current = x;
            while (true)
            {
                if (train[current].first == current)
                {
                    break;
                }
                else
                {
                    current = train[current].first;
                }
            }
            vector<int> ans;
            ans.push_back(current);
            while (true)
            {
                if (train[current].second == current)
                {
                    break;
                }
                else
                {
                    ans.push_back(train[current].second);
                    current = train[current].second;
                }
            }
            cout << ans.size();
            for (auto j : ans)
            {
                cout << " " << j;
            }
            cout << endl;
        }
    }
    return 0;
}