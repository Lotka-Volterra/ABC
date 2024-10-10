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
    int N, S, T;
    cin >> N >> S >> T;
    vector<int> num;
    rep(i, 2 * N)
    {
        num.push_back(i + 1);
    }
    // vector<ll> A, B, C, D;
    vector<pair<double, double>> zahyo;
    rep(i, N)
    {
        double a, b, c, d;
        cin >> a >> b >> c >> d;
        // A.push_back(a);
        // B.push_back(b);
        // C.push_back(c);
        // D.push_back(d);
        zahyo.push_back({a, b});
        zahyo.push_back({c, d});
    }
    double ans = 1 << 30;
    double distance_cache[2 * N][2 * N];

    do
    {
        double time = 0;
        // 訪問済みの点
        vector<bool> visited(2 * N, false);
        pair<double, double> current = {0, 0};

        double movedistance = 0;
        double distance = 0;
        rep(i, 2 * N)
        {
            int point = num[i] - 1;
            if (visited[point])
            {
                continue;
            }
            movedistance += sqrt(pow(zahyo[point].first - current.first, 2) + pow(zahyo[point].second - current.second, 2));

            int next_point;
            if (point % 2 == 0)
            {
                next_point = point + 1;
            }
            else
            {
                next_point = point - 1;
            }
            distance += sqrt(pow(zahyo[point].first - zahyo[next_point].first, 2) + pow(zahyo[point].second - zahyo[next_point].second, 2));
            current.first = zahyo[next_point].first;
            current.second = zahyo[next_point].second;
            visited[point] = true;
            visited[next_point] = true;
        }
        time += movedistance / S;
        time += distance / T;

        ans = min(time, ans);
    } while (next_permutation(num.begin(), num.end()));
    cout << ans << endl;
    return 0;
}