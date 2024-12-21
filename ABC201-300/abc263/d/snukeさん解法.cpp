#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;

int main()
{
    int n;
    ll L, R;
    cin >> n >> L >> R;
    vector<int> a(n);
    rep(i, n)
    {
        cin >> a[i];
    }
    ll ans = R * n; // 全てがRに置き換えた場合。Lの区間とAのままの区間が無い状態
    // sumaはA1からArまでの和。
    // sumbはA1からArまでをLで置き換えたときの差分。
    // maxbはLに置き換える区間を1からr-1まで動かしたときの差分の最大値。
    ll suma = 0, sumb = 0, maxb = 0;

    rep(r, n)
    {
        suma += a[r];
        sumb += a[r] - L;
        maxb = max(maxb, sumb);
        // suma-maxbで、0から(0-indexed)rまでをLの区間とAのままの区間で占めたときの最適な書き換え方の時の0からrまでの総和
        //  R*(n-r-1)で、残りの区間(Rの区間)の総和。0-indexedでr+1からn-1まで。n-1-(r+1-1)=n-r-1
        ll now = suma - maxb + R * (n - r - 1);
        ans = min(ans, now);
    }
    cout << ans << endl;
}
