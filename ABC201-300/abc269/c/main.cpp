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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N;
    cin >> N;
    map<int, int> A;
    // rep(i, N)
    // {
    //     cin >> A[i];
    // }
    // bool Answer = false;
    int count1 = 0;
    rep(i, 60)
    {
        if (N & (1LL << i)) // iと1<<jでAND演算。iの下からj桁目が2進数表記で1なら、真（非ゼロ）を返す
        {
            A[count1] = i;
            count1++;
        }
    }
    rep(i, 1 << count1) // i=0から1<<N-1まで全探索
    {
        vector<char> Ans(60, '0');
        rep(j, count1)
        {
            if (i & (1 << j)) // iと1<<jでAND演算。iの下からj桁目が2進数表記で1なら、真（非ゼロ）を返す
            {
                Ans[A[j]] = '1';
            }
        }
        string binaryStr = "";
        for (int j = 59; j >= 0; --j)
        {
            binaryStr += Ans[j];
        }
        // std::bitsetを使って2進数の文字列を10進数の数値に変換
        bitset<60> bitset(binaryStr); // 最大60ビットまで対応（必要に応じて調整可能）

        // bitsetをunsigned longとして取得し、出力
        unsigned long decimalValue = bitset.to_ulong();
        cout << decimalValue << endl;
    }

    return 0;
}