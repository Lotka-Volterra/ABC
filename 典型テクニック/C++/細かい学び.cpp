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

    // setの二分探索
    set<int> num;
    num.insert(1);
    num.insert(2);
    // set独自の二分探索をしないと、O(logN)にならない
    // https://qiita.com/sinzyousan/items/158b19a9a3fecf8b855f
    num.lower_bound(1);
    // イテレータは++や--で一つ大きい・小さい値に移動できる
    auto itr = num.lower_bound(1);
    itr++;
    cout << *itr << endl;
    // mapの最小値、最大値。setの最小値、最大値(O(1)つまり定数時間)
    set<int> s;
    // 最小値のイテレータを指定することで、最小値が取得できる
    *s.begin();
    // 最大値はrbegin(reverse begin)
    *s.rbegin();
    map<int, char> m;
    m[3] = 'C';
    m[7] = 'G';
    m[8] = 'H';
    m[4] = 'D';
    m[5] = 'E';
    m[1] = 'A';
    m[2] = 'B';
    m[6] = 'F';
    // ABCD...と出力される。つまり、キーが昇順
    for (auto i = m.begin(); i != m.end(); ++i)
    {
        cout << i->first << " " << i->second << "\n";
    }
    // 1 A
    // 2 B
    // 3 C
    // 4 D
    // 5 E
    // 6 F
    // 7 G
    // 8 H

    // ベクトルの重複する要素を削除する(setにする必要なし)
    const int M = 200010;

    vector<vector<int>> card(M, vector<int>());
    int i;
    cin >> i;
    sort(card[i].begin(), card[i].end());
    card[i].erase(unique(card[i].begin(), card[i].end()), card[i].end());
    // 1. unique(card[i].begin(), card[i].end()):
    // uniqueは、指定された範囲内の重複した連続する要素を削除する標準ライブラリの関数です。ここでは、card[i]ベクトルの最初（begin()）から最後（end()）までの範囲で重複する連続要素を削除します。
    // uniqueは削除された後の新しい終端イテレータを返します。この新しい終端イテレータは、実際にベクトルの要素を削除してはいませんが、重複していない要素の順序を保持したまま要素を前方に詰めます。
    // unique関数は、例えば [1, 2, 2, 3] のようなベクトルを [1, 2, 3, 3] にして、新しい終端イテレータは3の前（2つ目の3の位置）を指すことになります。
    // 2. erase(unique(...), card[i].end()):
    // **erase**関数は、ベクトルの範囲を指定して、その範囲の要素を削除します。eraseの引数に、unique関数が返した新しい終端イテレータと、end()を指定しています。
    // これにより、uniqueによって残った「重複した要素」を物理的にベクトルから削除します。

    // dequeの要素を順に出力
    deque<char> ans;
    for (auto it = ans.begin(); it != ans.end(); ++it)
    {
        cout << *it;
    }
    cout << endl;
    // ちなみに逆順（末尾から）出力する方法。rbegin,rendを使うだけ
    for (auto it = ans.rbegin(); it != ans.rend(); ++it)
    {
        cout << *it;
    }
    cout << endl;

    // ABC367 過剰なゼロを出力しない方法: double型で受け取る
    // 過剰なゼロを出力しないとは、0.00->0  0.600->0.6みたいなこと
    double x;
    cin >> x;
    cout << x << "\n";

    // 入力に必ず小数点がある制約(例えば123.000は入力される可能性があるが、123は入力されない)なので、下記の方法でも良い
    // 末尾が 0 である限り、その文字を削除することを繰り返す。
    // その後、末尾が . であればそれも削除する。
    string sx;
    cin >> sx;
    while (sx.back() == '0')
    {
        sx.pop_back();
    }
    if (sx.back() == '.')
    {
        sx.pop_back();
    }
    cout << x << "\n";

    // ABC233Dの公式解説
    // 連想配列の更新タイミングを変えると実装が楽になる(abc233/dにもメモあり)

    // 大きな数字
    ll bignumber = 1e18; //(10**18)
    return 0;
}