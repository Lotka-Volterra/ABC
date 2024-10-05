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
    // 鉄則本A20
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S, T;
    cin >> S >> T;
    int s = S.size(), t = T.size();
    vector<vector<int>> A(s + 1, vector<int>(t + 1, 0));
    rep(i, s + 1)
    {
        rep(j, t + 1)
        {
            // 右への移動
            if (j < t)
            {
                A[i][j + 1] = max(A[i][j + 1], A[i][j]);
            }
            // 下への移動
            if (i < s)
            {
                A[i + 1][j] = max(A[i + 1][j], A[i][j]);
            }
            // 右下への移動
            // SとTのインデックスと、Aのインデックスはずれている
            if (j < t && i < s && S[i] == T[j])
            {
                A[i + 1][j + 1] = A[i][j] + 1;
            }
        }
    }
    int ans = 0;
    rep(i, t + 1)
    {
        ans = max(ans, A[s][i]);
    }
    cout << ans << endl;
    return 0;
}