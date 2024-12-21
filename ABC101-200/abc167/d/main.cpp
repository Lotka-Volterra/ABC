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
    // 解説配信:周期で解く
    // 1周期は高々N個
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        int a;
        cin >> a;
        a--;
        A[i] = a;
    }

    vector<int> s;           // 訪れた街を順番に格納
    vector<int> ord(N, -1);  // ord[i]が街iを訪れた際の周期の中の順番(sの中でのインデックスに対応)
    int c = 1, l = 0;        // cは周期
    int v = 0;               // 初期位置1
    {                        // スコープを切る(名前空間の衝突を避けるためらしい)
        while (ord[v] == -1) // テレポート先が訪れたことがない間(まだ周期が1周していない場合)ループ
        {
            ord[v] = s.size();
            s.push_back(v);
            v = A[v]; // 次の街
        }
        c = s.size() - ord[v]; // 周期はs.size()からvを始めに訪れた時(0-indexed)
        l = ord[v];            // lは例外部分(周期が始まってない箇所)の長さ
    }

    if (K < l) // Kが周期に入っていない値の時
    {
        cout << s[K] + 1 << endl; // 1-indexedに戻すため1を足す
    }
    else
    {
        K -= l;                       // Kから周期に入っていない部分の長さを引く
        K %= c;                       // modを取り、周期内での位置を算出
        cout << s[l + K] + 1 << endl; // 1-indexedに戻すため1を足す
    }

    return 0;
}