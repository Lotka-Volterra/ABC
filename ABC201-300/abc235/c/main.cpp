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
    map<int, vector<int>> M;
    vector<int> A(N + 1, 0);
    for (int i = 1; i < N + 1; i++)
    {
        cin >> A[i];
        if (M.find(A[i]) != M.end())
        {
            M[A[i]].push_back(i);
        }
        else
        {
            M[A[i]] = {i};
        }
    }
    rep(i, Q)
    {
        int x, k;
        cin >> x >> k;
        if (M.find(x) != M.end() && M[x].size() >= k)
        {
            cout << M[x][k - 1] << endl;
        }
        else
        {
            cout << -1 << endl;
        }
    }
    return 0;
}