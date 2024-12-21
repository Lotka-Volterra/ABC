#include <stdio.h>
#define ll long long
#define max(p, q) ((p) > (q) ? (p) : (q))

ll dp[5][100010];
ll x[100010], a[100010];
// https://atcoder.jp/contests/abc266/submissions/34146266
int main()
{
    int n;
    scanf("%d", &n);
    // N回のイベントがあるが、これをイベントだけまとまった配列に格納するのではなく、
    // 全体の時間軸の配列(時間軸としては10**5秒まで)を作っておき、
    // そのイベントが起きる時刻のindexに要素を入れるという実装方法。
    // これにより、時間軸についてのFor文の中でイベントだけまとまった配列について別の進め方をするFor文を実装しなくて良い
    for (int i = 0; i < n; i++)
    {
        int t, xx, aa;
        scanf("%d%d%d", &t, &xx, &aa);
        x[t] = xx;
        a[t] = aa;
    }

    for (int i = 1; i < 5; i++)
        dp[i][0] = -1e18;

    for (int t = 1; t <= 100000; t++)
    {
        for (int i = 0; i < 5; i++)
        {
            dp[i][t] = dp[i][t - 1];
            if (i != 0)
                dp[i][t] = max(dp[i][t], dp[i - 1][t - 1]);
            if (i != 4)
                dp[i][t] = max(dp[i][t], dp[i + 1][t - 1]);
        }
        dp[x[t]][t] += a[t]; // イベントがある場合は、その値、なければ、初期値0が足されるだけで結果に影響しない
    }

    ll ans = 0;
    for (int i = 0; i < 5; i++)
        ans = max(ans, dp[i][100000]);
    printf("%lld\n", ans);
}