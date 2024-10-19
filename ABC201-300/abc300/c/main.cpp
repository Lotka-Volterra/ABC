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
    ll H, W;
    cin >> H >> W;
    vector<vector<char>> C(H, vector<char>(W));
    rep(i, H)
    {
        rep(j, W)
        {
            cin >> C[i][j];
        }
    }
    vector<int> Ans(min(H, W) + 1, 0);
    for (int i = 1; i < H - 1; i++)
    {
        for (int j = 1; j < W - 1; j++)
        {
            if (C[i - 1][j - 1] == '#' && C[i - 1][j] == '.' && C[i - 1][j + 1] == '#' && C[i][j - 1] == '.' && C[i][j] == '#' && C[i][j + 1] == '.' && C[i + 1][j - 1] == '#' && C[i + 1][j] == '.' && C[i + 1][j + 1] == '#')
            {
                int count = 1;
                for (int k = 2; k <= min(H, W); k++)
                {
                    if (i + k < H && j + k < W && C[i + k][j + k] == '#')
                    {
                        count++;
                    }
                    else
                    {
                        break;
                    }
                }
                Ans[count]++;
            }
        }
    }
    for (int i = 1; i <= min(H, W); i++)
    {
        if (i != 1)
        {
            cout << " ";
        }

        cout << Ans[i];
    }
    cout << endl;
    return 0;
}