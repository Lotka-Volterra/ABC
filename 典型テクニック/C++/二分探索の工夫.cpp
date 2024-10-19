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
// ABC136D
// 二分探索の結果、コンテナ.end()が返ってきた時、それをデリファレンスして未定義動作を引き起こし、WAになっていた。(これは解決済みのコード)
// 無理やりデリファレンスするくらいなら、最初から正負を反転させて、ソートさせて二分探索をすることで、同じ値かそれ以上の値を取得できる。
// 今回は問題の性質上、正負を反転させれば、lower_boundでコンテナ.end()が返ってこないので実装も省力化できる
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S;
    cin >> S;
    vector<int> L;
    vector<int> R;
    int N = (int)S.size();
    rep(i, N - 1)
    {
        if (S[i] == 'R' && S[i + 1] == 'L')
        {
            R.push_back(i);
            L.push_back(-(i + 1));
        }
    }
    sort(L.begin(), L.end());
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
            int l = -*lower_bound(L.begin(), L.end(), -i);
            if ((i - l) % 2 == 0)
            {
                ans[l]++;
            }
            else
            {
                ans[l - 1]++;
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