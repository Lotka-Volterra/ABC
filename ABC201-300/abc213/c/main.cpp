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
// ABC213 C
// 座標圧縮(数字の書かれていない、行と列を詰める)
// *****
// ****2
// *1***
// *****
//   ↓
// *2
// 1*
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int H, W, N;
    cin >> H >> W >> N;
    // 行と列の情報を格納するvector
    vector<pair<int, int>> AB;
    // 行だけ（圧縮のため集合を使う）
    set<int> A;
    // 列だけ
    set<int> B;
    // 連想配列で、圧縮前の座標と圧縮後の座標を関連付ける
    map<int, int> a_order;
    map<int, int> b_order;

    rep(i, N)
    {
        int a, b;
        cin >> a >> b;
        A.insert(a);
        B.insert(b);
        AB.push_back({a, b});
    }
    // 座標圧縮は、大小関係を保ったまま値を小さくする操作。
    // 使われていない行（あるいは列）を削除する操作は、大小関係を保ったまま値を小さくする操作と同じ
    // 行だけ、列だけでソートする。
    vector<int> vecA(A.begin(), A.end());
    vector<int> vecB(B.begin(), B.end());

    sort(vecA.begin(), vecA.end());
    sort(vecB.begin(), vecB.end());

    // たとえば、行が[3, 1, 5] なら[1, 3, 5] になっている状態。
    // 圧縮すると、行1 = 1番目、行3 = 1番目、行5 = 3番目の行になる。この対応付けに連想配列を用いる
    // x座標,y座標について、それぞれ数字が小さい順に1,2,と番号を付与する
    // 行の削除、列の削除は独立なため、x座標とy座標それぞれで処理を行って良い
    rep(i, vecA.size())
    {
        a_order[vecA[i]] = i + 1;
    }
    rep(i, vecB.size())
    {
        b_order[vecB[i]] = i + 1;
    }
    // それぞれの点について、x座標、y座標ごとに連想配列から圧縮後の番号を取得して出力
    rep(i, N)
    {
        cout << a_order[AB[i].first] << " " << b_order[AB[i].second] << endl;
    }
}