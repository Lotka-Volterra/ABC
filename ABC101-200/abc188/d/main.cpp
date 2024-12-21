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
vector<ll> input(int N)
{
    vector<ll> vec(N);
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
    ll N, C;
    cin >> N >> C;
    map<ll, ll> A;
    // imos法
    rep(i, N)
    {
        ll a, b, c;
        cin >> a >> b >> c;
        if (A.find(a) != A.end())
        {
            A[a] += c;
        }
        else
        {
            A[a] = c;
        }
        if (A.find(b + 1) != A.end())
        {
            A[b + 1] -= c;
        }
        else
        {
            A[b + 1] = -c;
        }
    }
    // 最初の日
    ll preDate = A.begin()->first;
    // サブスクリプションだけの料金
    ll sumPrice = A.begin()->second;

    auto itr = A.begin();
    itr++;
    ll ans = 0LL;
    for (auto i = itr; i != A.end(); ++i)
    {
        ll nowDate = i->first;
        ll nowPrice = i->second;
        ans += min(C, sumPrice) * (nowDate - preDate);
        preDate = nowDate;
        sumPrice = sumPrice + nowPrice;
    }
    cout << ans << endl;
}