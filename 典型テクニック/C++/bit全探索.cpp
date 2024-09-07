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
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    rep(i, N)
    {
        cin >> A[i];
    }
    bool Answer = false;
    rep(i, 1 << N) // i=0から1<<N-1まで全探索
    {
        int sum = 0;
        rep(j, N)
        {
            if (i & (1 << j)) // iと1<<jでAND演算。iの下からj桁目が2進数表記で1なら、真（非ゼロ）を返す
            {
                sum += A[j];
            }
        }
        if (sum == K)
        {
            Answer = true;
            break; // 一致したらすぐにループを抜ける
        }
    }
    if (Answer)
        Yes;
    else
        No;

    return 0;
}