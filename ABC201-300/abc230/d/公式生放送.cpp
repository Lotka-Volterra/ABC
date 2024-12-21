#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<ll, ll>;
int main()
{
    ll N, D;
    vector<P> RL(N);
    cin >> N >> D;
    for (int i = 0; i < N; i++)
    {
        cin >> RL[i].second >> RL[i].first; // first=R,second=Lと逆に入れておけば、sortで比較用の関数を渡す必要がない
    }
    sort(RL.begin(), RL.end());
    ll ans = 0, x = -1LL;
    for (auto &[r, l] : RL)
    {
        if (l <= x) // 壁にxが含まれているかどうか。rの昇順のため、x<=rは考える必要がない
        {
            continue;
        }
        ++ans;
        x = r + D - 1; // パンチの破壊範囲を広げることで、D=1の問題に帰着させる。
    }
    cout << ans << "\n";
}
