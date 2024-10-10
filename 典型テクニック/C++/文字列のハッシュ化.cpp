#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using Graph = vector<vector<int>>;
// using namespace atcoder;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
// usage:rep(i,3){ processing }  i starts at 0 and increments by 1 until it reaches n.
#define rep1(i, n) for (int i = 1; i < (int)(n); i++)
// usage:rep(i,3){ processing }  i starts at 1 and increments by 1 until it reaches n.
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
// usage:rep2(i,1,3){ processing }  i starts at s and increments by 1 until it reaches n.
#define Yes cout << "Yes" << endl
#define No cout << "No" << endl
#define YES cout << "YES" << endl
#define NO cout << "NO" << endl
// 無限大を表す値
const ll INF = 1LL << 60; // 十分大きな値を用いる(ここでは2^60)
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
// aの階乗a!を返す
ll factorial(ll a)
{
    ll ans = 1;
    rep1(i, a + 1)
    {
        ans *= i;
    }
    return ans;
}
// aの階乗a!をmで割った余りを返す
ll factorial_mod(ll a, ll m)
{
    ll ans = 1;
    rep1(i, a + 1)
    {
        ans = ans * i % m;
    }
    return ans;
}
// a**bをmで割った余りを返す
ll power_mod(ll a, ll b, ll m)
{
    // pはa**1,a**2,a**4と変化
    ll p = a, ans = 1LL;
    // bは10**9以下とする。そのため、iは2**30>10**9まで
    // しっくりこなかったら鉄則本A29の実装にする
    rep(i, 30)
    {
        if (b == 0)
        {
            break;
        }
        if (b % 2 == 1)
        {
            ans = ans * p % m;
        }
        p = p * p % m;
        b /= 2;
    }
    return ans;
}
// 文字列のハッシュ（鉄則本A56）
// 余りを求めるときに使う割る数
ll mod = 2714783647LL;
// Tが文字列をインデックス1から入れたもの（-'a'などで数値に変換）
// Hashがハッシュ化した値の途中計算に使う配列。インデックス1からはじまり、1からi文字目までのハッシュ値
// Power100が100のn乗を前計算した結果を格納する配列。ハッシュ値の計算時に使用する
ll T[200009], Hash[200009], Power100[200009];

// 文字列のl文字目からr文字目のハッシュ値を返す。ハッシュ値は100進数に変換してmodで割った余り
ll hash_value(int l, int r)
{
    ll val = Hash[r] - (Hash[l - 1] * Power100[r - l + 1] % mod);
    if (val < 0)
    {
        val += mod;
    }
    return val;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // hash_valueの事前準備用処理
    string S;
    cin >> S;
    int N;
    cin >> N;
    rep1(i, N + 1)
    {
        // 文字列Sのi-1文字目（Sはインデックス0からなので、インデックス1からのT用に整形）の英小文字を数値に変換
        // a=1,b=2,...,z=26
        T[i] = (S[i - 1] - 'a') + 1;
    }
    // 100の0乗として1を設定
    Power100[0] = 1;
    // 100のn乗まで計算。ハッシュ値の計算時は余りを用いるので、modで割ってよい
    rep1(i, N + 1)
    {
        Power100[i] = 100LL * Power100[i - 1] % mod;
    }
    // i文字目までのハッシュ値を計算する
    Hash[0] = 0;
    rep1(i, N + 1)
    {
        // i文字目までのハッシュ値は、i-1文字目までのハッシュ値を左シフトさせてi文字目を足してmodで割った余りに等しい
        Hash[i] = (100LL * Hash[i - 1] + T[i]) % mod;
    }
    return 0;
}