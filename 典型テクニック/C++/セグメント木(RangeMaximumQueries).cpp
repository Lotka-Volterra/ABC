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
// 鉄則本A58
class SegmentTree
{
public:
    int dat[300000], siz = 1;
    void init(int N)
    {
        siz = 1;
        // sizはNより大きい2の累乗の中で最小の数とする
        while (siz < N)
        {
            siz *= 2;
        }
        // 要素datの初期化を行う(最初は全部0)
        for (int i = 1; i < siz * 2; i++)
        {
            dat[i] = 0;
        }
    }
    // クエリ1に対する処理
    void update(int pos, int x)
    {
        // pos個目の要素だけが含まれるセルの番号
        pos = pos + siz - 1;
        dat[pos] = x;
        // 根にたどり着くまで
        while (pos >= 2)
        {
            pos /= 2;                                       // 親の階層に登る
            dat[pos] = max(dat[pos * 2], dat[pos * 2 + 1]); // もともと居たセルと、隣接するセルの最大値を、現在位置である親のセルの最大値とする
        }
    }
    // クエリ2に対する処理
    // [l,r)は求めたい半開区間,uは現在のセル番号,[a,b)はセルに対応する半開区間
    int query(int l, int r, int a, int b, int u)
    {
        // [l,r)が[a,b)に一切含まれない場合
        if (r <= a || b <= l)
        {
            return -1000000000; // 最大値の計算に影響しないような負の値を返す
        }
        // [l,r)が[a,b)に完全に含まれる場合
        if (l <= a && b <= r)
        {
            return dat[u]; // そのセルの値を返す
        }
        // 子セルの境界値
        int m = (a + b) / 2;
        // 左下のセルの値を求める
        int AnswerL = query(l, r, a, m, u * 2);
        // 右下のセルの値を求める
        int AnswerR = query(l, r, m, b, u * 2 + 1);
        return max(AnswerL, AnswerR);
    }
};
SegmentTree Z;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    cin >> N >> Q;
    Z.init(N);
    rep(i, Q)
    {
        ll q, l, r;
        cin >> q >> l >> r;
        if (q == 1)
        {
            Z.update(l, r);
        }
        else
        {
            // 最初のセルに対応する半開区間は[1,siz+1)。最初のセル番号は1
            int ans = Z.query(l, r, 1, Z.siz + 1, 1);
            cout << ans << endl;
        }
    }
    return 0;
}