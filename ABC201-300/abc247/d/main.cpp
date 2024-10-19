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
vector<int> input(int N)
{
    vector<int> vec(N);
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
    int Q;
    cin >> Q;
    deque<pair<ll, ll>> q;
    rep(i, Q)
    {
        int type;
        cin >> type;
        if (type == 1)
        {
            ll x, c;
            cin >> x >> c;
            q.push_back({x, c});
        }
        else
        {
            ll c;
            cin >> c;
            ll ans = 0;
            while (c > 0)
            {
                // 先頭要素の個数を取得
                ll count = q.front().second;
                // 先頭要素の個数と、cの大きさの最小値を取る。
                ll reduceCount = min(count, c);
                c -= reduceCount;
                ans += q.front().first * reduceCount;
                // 先頭要素の個数を減らす
                q.front().second -= reduceCount;
                // 先頭要素の個数が0になったら、先頭から削除する
                if (reduceCount == count)
                {
                    q.pop_front();
                }
            }

            cout << ans << endl;
        }
    }

    return 0;
}