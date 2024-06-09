#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    for (int i = 0; i < M; i++)
    {
        cin >> A.at(i) >> B.at(i);
    }

    // ここにプログラムを追記
    // (ここで"試合結果の表"の2次元配列を宣言)
    vector<vector<char>> result(N, vector<char>(N, '-'));
    rep(i, M)
    {
        result[A[i] - 1][B[i] - 1] = 'o';
        result[B[i] - 1][A[i] - 1] = 'x';
    }
    rep(i, N)
    {
        rep(j, N)
        {
            cout << result[i][j];
            if (j == N - 1)
            {
                cout << endl; // 末尾なら改行
            }
            else
            {
                cout << " "; // それ以外なら空白
            }
        }
    }
    return 0;
}