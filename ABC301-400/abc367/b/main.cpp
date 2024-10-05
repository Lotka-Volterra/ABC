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
    string X;
    cin >> X;
    auto ans = vector<char>();
    // 逆順にして末尾から見る
    reverse(X.begin(), X.end());
    // ゼロ以外フラグ。ゼロ以外の数字が初めて出てきた時trueになる
    bool zeroIgaiFlag = false;
    // 0は例外的に処理
    if (X == "0")
    {
        cout << 0 << endl;
        return 0;
    }

    rep(i, X.size())
    {
        if (!zeroIgaiFlag)
        {
            if (X[i] == '0')
            {
                continue;
            }
            else if (X[i] == '.')
            {
                zeroIgaiFlag = true;
            }
            else
            {
                ans.push_back(X[i]);
            }
        }
        else
        {
            ans.push_back(X[i]);
        }
    }
    reverse(ans.begin(), ans.end());
    rep(i, ans.size())
    {
        cout << ans[i];
    }
    cout << endl;
    return 0;
}