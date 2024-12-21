#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, l, r) for (ll i = l; i <= r; i++)
// https://atcoder.jp/contests/abc233/editorial/3163
signed main()
{
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    rep(i, 0, n - 1) cin >> a[i];
    vector<ll> s(n + 1);
    rep(i, 0, n - 1) s[i + 1] = s[i] + a[i]; // 累積和
    map<ll, ll> mp;                          // 連想配列
    ll ans = 0;
    // ポイント1:rから見て考えるので、S[r]-kを見つければ良いので(個人的に)シンプル
    // ポイント2:r時点までの連想配列の更新->連想配列の参照、という順序のため、
    // 余計なインデックス(rより大きいインデックスで、S[r]-kを満たすもの)が入っていない
    rep(r, 1, n)
    {
        mp[s[r - 1]]++;
        ans += mp[s[r] - k];
    }
    cout << ans << endl;
    return 0;
}
