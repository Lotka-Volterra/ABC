#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    ll H, W;
    cin >> H >> W;
    ll ans = H * W;
    if (H % 3 == 0 || W % 3 == 0)
    {
        ans = 0;
    }
    else
    {
        ll b = W / 2;
        for (ll a = 1; a <= H / 2 + 1; a++)
        {
            ll chohoke1 = a * W, chohoke2 = (H - a) * b, chohoke3 = (H - a) * (W - b);
            ans = min(ans, max({chohoke1, chohoke2, chohoke3}) - min({chohoke1, chohoke2, chohoke3}));
        }
        ll d = H / 2;
        for (ll c = 1; c <= W / 2 + 1; c++)
        {
            ll chohoke1 = c * H, chohoke2 = (W - c) * d, chohoke3 = (W - c) * (H - d);
            ans = min(ans, max({chohoke1, chohoke2, chohoke3}) - min({chohoke1, chohoke2, chohoke3}));
        }
    }
    cout << ans << endl;
    return 0;
}
