#include <bits/stdc++.h>

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
    vector<int> a = {1, 4, 4, 7, 7, 8, 8, 11, 13, 19};
    // lower_boundは、key以上の値を持つ一番左のイテレータを返す。
    // uppder_boundは、keyより大きい値を持つ一番左のイテレータを返す。
    auto Iter1 = *lower_bound(a.begin(), a.end(), 4); // *をつけることで要素にアクセスしている。4になる
    auto Iter2 = *upper_bound(a.begin(), a.end(), 4); // 7になる
    // 先頭からの距離を測ることもできる
    // 先頭からの距離とは、その要素より小さい要素の個数
    // また、これはインデックス番号と一致する(0-indexed)
    auto Iter11 = lower_bound(a.begin(), a.end(), 4);
    auto Iter21 = upper_bound(a.begin(), a.end(), 4);
    cout << "Iter11 = " << Iter11 - a.begin() << endl; // Iter1 = 1。4より小さい要素の個数は1個
    cout << "Iter21 = " << Iter21 - a.begin() << endl; // Iter2 = 3。4以下の要素の個数は3個
    // 末尾からの距離を測ることもできる
    // 末尾からの距離とは、その要素以上の要素の個数
    cout << "Iter11 = " << a.end() - Iter11 << endl; // Iter1 = 9。4以上の要素の個数は9個
    cout << "Iter21 = " << a.end() - Iter21 << endl; // Iter1 = 9。4より大きい要素の個数は7個

    // lower_boundの挙動
    // vector<int> Aの最初の要素よりも探索する数xが小さい場合は、A.begin()を返す。これはkey以上の値がA.begin()であるため。
    // Aの末尾の要素よりも探索する数xが大きい場合は、A.end()を返す。A.end()はコンテナAの末尾の次の要素であり、イテレータの終了条件でもある。
    return 0;
}