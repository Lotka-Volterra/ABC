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
    int N, D;
    cin >> N >> D;
    auto X = vector<int>(N), Y = vector<int>(N);
    int x, y;
    rep(i, N)
    {
        cin >> x >> y;
        X[i] = x;
        Y[i] = y;
    }
    auto infected = vector<bool>(N);
    auto checked = vector<bool>(N);
    vector<int> infected_people = {0};
    D = D * D;
    while (infected_people.size() != 0)
    {
        auto target = infected_people.back();
        infected_people.pop_back();
        infected[target] = true;
        checked[target] = true;
        rep(i, N)
        {
            if (checked[i])
            {
                continue;
            }
            int distance = pow((X[i] - X[target]), 2) + pow((Y[i] - Y[target]), 2);
            if (distance <= D && !infected[i])
            {
                infected[i] = true;
                infected_people.push_back(i);
            }
        }
    }
    rep(i, N)
    {
        if (infected[i])
        {
            Yes;
        }
        else
        {
            No;
        }
    }
}