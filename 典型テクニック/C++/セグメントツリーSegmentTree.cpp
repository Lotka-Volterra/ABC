#include <iostream>
#include <vector>
#include <functional>
using namespace std;

// https://drken1215.hatenablog.com/entry/2019/04/27/224100_1
// モノイドとは、結合的二項演算(任意の要素の順序付けられた3つ組が結合すること。a*(b*c)=(a*b)*cが成立する。例:加算、乗算)が可能で、
// 単位元(例:加算における0,乗算における1)が存在する組。

// セグメントツリー
template <class Monoid>
struct SegTree
{
    using Func = function<Monoid(Monoid, Monoid)>;
    const Func F;       // 結合的二項演算
    const Monoid UNITY; // 単位元
    int SIZE_R;         // 葉の大きさ
    vector<Monoid> dat;

    SegTree(int n, const Func f, const Monoid &unity) : F(f), UNITY(unity) { init(n); } // FとUNITYを引数で初期化
    void init(int n)
    {
        SIZE_R = 1;
        while (SIZE_R < n)
            SIZE_R *= 2;               // 葉の大きさは、n以上の最小の2の累乗とする
        dat.assign(SIZE_R * 2, UNITY); // 葉はSIZE_R枚、内部ノードはSIZE_R - 1個。内部ノードのIndexは1から始まり、SIZE_R - 1まで。単位元で初期化。
    }

    /* set, a is 0-indexed */
    // index a番目の要素に値vを設定する
    void set(int a, const Monoid &v) { dat[a + SIZE_R] = v; } // 葉はSIZE_R番目から開始して、SIZE_R+N-1番目まで
    void build()
    {
        // 内部ノードのIndexは1から始まり、SIZE_R - 1まで
        // 内部ノードをSIZE_R-1から1まで、下から結合的二項演算を繰り返す
        for (int k = SIZE_R - 1; k > 0; --k)
            dat[k] = F(dat[k * 2], dat[k * 2 + 1]);
    }

    /* update a, a is 0-indexed */
    // index a番目の要素を値vに更新する
    void update(int a, const Monoid &v)
    {
        int k = a + SIZE_R;
        dat[k] = v;
        while (k >>= 1) // kが根(1)でない限り、2の1乗すなわち2で割ることで、親ノードに行く。
            dat[k] = F(dat[k * 2], dat[k * 2 + 1]);
    }

    /* get [a, b), a and b are 0-indexed */
    Monoid get(int a, int b)
    {
        Monoid vleft = UNITY, vright = UNITY;
        // left<rightの間、left,rightをそれぞれ親ノードに登らせていく
        for (int left = a + SIZE_R, right = b + SIZE_R; left < right; left >>= 1, right >>= 1)
        {
            // lef&1がtrueつまりleftが奇数の場合、結合的二項演算を行い、leftをインクリメント。
            // これは、左からの区間を考えるうえでleftが奇数の場合、親ノードではなく、親の右のノードに行きたいから。
            // vleftに値を保存してからインクリメントすることで、親の右ノードへ進める
            if (left & 1)
                vleft = F(vleft, dat[left++]);
            // rightが奇数の場合、rightをデクリメントし、結合的二項演算を行なう
            // 前提として、右は開区間である。求める区間に含まれるのはbの一つ左の要素である。
            // 右からの区間を考えるうえでrightが奇数の場合、実際に含まれるのはその左の要素(偶数)である。その要素は親の左のノードに行きたい。
            // デクリメントしてからvrightに値を保存して、次のループで親の左ノードへ進める
            if (right & 1)
                vright = F(dat[--right], vright);
        }
        return F(vleft, vright); // vleft,vrightで演算
    }
    // tree[a]で葉のa番目の要素の値にアクセスできるようにする
    inline Monoid operator[](int a) { return dat[a + SIZE_R]; }

    /* debug */
    // 葉の要素だけをカンマ区切りで出力
    void print()
    {
        for (int i = 0; i < SIZE_R; ++i)
        {
            cout << (*this)[i];
            if (i != SIZE_R - 1)
                cout << ",";
        }
        cout << endl;
    }
};

// ユークリッドの互除法のアルゴリズム。
// a>=bの前提で、bが0でない場合、a=b,b=a%bに置き換えて自身を再帰的に呼び出す。
// bが0の場合、aを返す
// a<bの場合も、a%b==aにより、次のループでaとbが入れ替わる
// そのため、a=0,b>0の場合でも、次のループに行って(元aが入れ替わった)b=0によりa(元b)が返される
long long GCD(long long a, long long b)
{
    return b ? GCD(b, a % b) : a;
}

int main()
{
    int N;
    cin >> N;

    // セグツリーの構築
    SegTree<long long> seg(N, [](long long a, long long b)
                           { return GCD(a, b); }, 0);
    vector<long long> A(N);
    for (int i = 0; i < N; ++i)
    {
        cin >> A[i];
        seg.set(i, A[i]);
    }
    seg.build();

    // 求める
    long long res = 0;
    for (int i = 0; i < N; ++i)
    {
        long long left = seg.get(0, i);
        long long right = seg.get(i + 1, N);
        res = max(res, GCD(left, right));
    }
    cout << res << endl;
}