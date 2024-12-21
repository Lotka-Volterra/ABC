#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<ll, ll>;
int main()
{
    ll N, D, L, R;
    vector<P> LR;
    cin >> N >> D;
    for (int i = 0; i < N; i++)
    {
        cin >> L >> R;
        LR.emplace_back(L, R); // first=R,second=Lと逆に入れておけば、17-18行目で比較用の関数を渡す必要がない
    }
    sort(begin(LR), end(LR), [](P &a, P &b)
         { return a.second < b.second; });
    ll ans = 0, x = -(1LL << 40);
    for (auto &[l, r] : LR)
    {
        if (x + D - 1 < l) // Rで昇順ソートしているので、xは単調増加。見るべきはx+D-1<l(壁が破壊されていないかどうか)
            ans++, x = r;
    }
    cout << ans << "\n";
}
