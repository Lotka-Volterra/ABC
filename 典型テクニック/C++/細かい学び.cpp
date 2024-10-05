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
    cout << endl; // 最後に改行　これによって、If文などで分岐させる必要がない
    int N, K, A[22];
    cin >> N >> K;
    for (int i = 0; i < N; i++)
    {
        cin >> A[i]; // 直接配列に代入する。別の変数にcinしてから代入する必要がない
    }
    // 位取りに'が使える
    int right = 1'000'000'000;
    // charを数字に変換するには、'0'を引く
    (int)('9' - '0');
    // stringを数字に変換するには、string to int(stoi)
    stoi("9");
    // アルファベット→数字の変換
    char c = 'a';
    c - 'a';

    // オーバーフロー
    // 最終的にlong型の変数aに代入するとしても、int型とint型の計算結果を一旦int型として保持するので、オーバーフローは起きる
    // 掛け算をする前に片方をlong型にキャストすることが必要
    int n = 50000;
    long a = n * n;
    long b = (long)n * n;
    return 0;
}