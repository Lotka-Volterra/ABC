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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    priority_queue<int> que;
    int N, M;
    cin >> N >> M;
    rep(i, N)
    {
        int a;
        cin >> a;
        que.push(a);
    }

    for (int i = 0; i < M; i++)
    {
        if (que.empty())
        {
            break;
        }
        int top = que.top();
        que.pop();
        top /= 2;
        que.push(top);
    }
    ll ans = 0LL;
    while (!que.empty())
    {
        ans += que.top();
        que.pop();
    }
    cout << ans << endl;

    return 0;
}