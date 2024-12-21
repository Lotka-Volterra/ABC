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

int main()
{
    // ABC130D
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N, K;
    cin >> N >> K;
    vector<ll> A(N + 1);
    A[0] = 0LL;
    // A[i]にi番目を入れて、インデックスとAiを合わせる
    for (int i = 1; i < N + 1; i++)
    {
        cin >> A[i];
    }
    vector<ll> ruiseki(N + 1);
    ruiseki[0] = 0LL;
    for (int i = 1; i < N + 1; i++)
    {
        ruiseki[i] = ruiseki[i - 1] + A[i];
    }

    // 尺取の到達点を記録
    vector<ll> R(N);
    // 0からN-1まで尺取の後ろ足部分を動かす。累積和のため0からスタート
    for (int i = 0; i < N; i++)
    {
        // i=1の場合は、尺取の前足のスタート地点は1。それ以外の場合は、前足のスタート地点はR[i-1]
        if (i == 0)
        {
            R[i] = 0; // 累積和のため0からスタート(A[1]>=Kを考慮)
        }
        else
        {
            R[i] = R[i - 1];
        }
        // 前足(R[i])がN未満かつ、次の前足の到達地点が条件(A[i]+K)を満たしている限り処理を続ける
        while (R[i] < N && ruiseki[R[i] + 1] - ruiseki[i] < K)
        {
            R[i]++;
        }
    }

    ll ans = 0;
    for (int i = 0; i < N; i++)
    {
        ans += N - R[i];
    }
    cout << ans << endl;
    return 0;
}