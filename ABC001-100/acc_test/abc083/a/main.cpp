#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // 4つの整数を格納する変数を宣言
    int a, b, c, d;

    // 標準入力から4つの整数を読み込む
    std::cin >> a >> b >> c >> d;

    // 最初の2数の和と残りの2数の和を計算
    int sum1 = a + b;
    int sum2 = c + d;

    // 条件に応じて結果を出力
    if (sum1 > sum2)
    {
        std::cout << "Left\n";
    }
    else if (sum1 == sum2)
    {
        std::cout << "Balanced\n";
    }
    else
    {
        std::cout << "Right\n";
    }
    return 0;
}