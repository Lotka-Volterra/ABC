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
// 鉄則本B26から。N以下の素数を出力する
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    // すでに検証した素数の倍数かどうかを判定する。trueなら素数ではない
    vector<bool> deleted(N + 1, false);
    // 素数なので2からスタート
    for (int i = 2; i * i <= N; i++)
    {
        // i*2からNまで、iの倍数を消していく
        for (int j = i * 2; j <= N; j += i)
        {
            deleted[j] = true;
        }
    }
    for (int i = 2; i <= N; i++)
    {
        if (!deleted[i])
        {
            cout << i << endl;
        }
    }

    return 0;
}