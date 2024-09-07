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
    int N;
    cin >> N;
    char S[N][100];
    // まず全部*にする
    rep(i, 100)
    {
        rep(j, 100)
        {
            S[i][j] = '*';
        }
    }
    // 各列のここまで文字という情報を格納
    int dict[100];
    rep(i, 100)
    {
        dict[i] = -1;
    }
    rep(i, N)
    {
        string Si;
        cin >> Si;
        rep(j, Si.size())
        {
            {
                S[i][j] = Si[j];
            }
        }
    }
    rep(i, 100)
    {
        int index = -1;
        rep(j, N)
        {
            if (S[j][i] != '*')
            {
                index = j;
            }
        }
        dict[i] = index;
    }
    rep(i, 100)
    {
        // 文字があるところまで出力
        rep(j, dict[i] + 1)
        {
            cout << S[i][j];
        }
        cout << endl;
    }
    return 0;
}