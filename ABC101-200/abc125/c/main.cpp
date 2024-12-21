#include <iostream>
#include <vector>
using namespace std;

template <class T>
inline bool chmax(T &a, T b)
{
    if (a < b)
    {
        a = b;
        return 1;
    }
    return 0;
}

// ユークリッドの互除法のアルゴリズム。
// a>=bの前提で、bが0でない場合、a=b,b=a%bに置き換えて自身を再帰的に呼び出す。
// bが0の場合、aを返す
// a<bの場合も、a%b==aにより、次のループでaとbが入れ替わる
// そのため、a=0,b>0の場合でも、次のループに行って(元aが入れ替わった)b=0によりa(元b)が返される
int GCD(int a, int b) { return b ? GCD(b, a % b) : a; }

int main()
{
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; ++i)
        cin >> a[i];

    // 累積 GCD (左と右両方)
    vector<int> left(N + 1, 0), right(N + 1, 0);
    // left[p]=区間[0,p)の最大公約数
    // left[0]=0,left[1]=区間[0,1)=a[0]
    for (int i = 0; i < N; ++i)
        left[i + 1] = GCD(left[i], a[i]);
    // right[p]=区間[p,N)の最大公約数(添字iが0からN-1までなので、実質的には区間[p,N-1])
    // right[N]=0,right[N-1]=区間[N-1,N)=a[N-1]
    for (int i = N - 1; i >= 0; --i)
        right[i] = GCD(right[i + 1], a[i]);

    // 集計
    int res = 0;
    for (int i = 0; i < N; ++i)
    {
        // a[i]を除いたN-1数の最大公約数を求める
        // 左側 区間[0,i)=区間[0,i-1]
        int l = left[i];

        // 右側 区間[i+1,N)=区間[i+1,N-1]
        int r = right[i + 1];

        // 更新
        chmax(res, GCD(l, r));
    }
    cout << res << endl;
}