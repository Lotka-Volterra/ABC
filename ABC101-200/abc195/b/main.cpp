#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int A, B, W;
    cin >> A >> B >> W;
    W *= 1000;
    int ans_min = (W + B - 1) / B;
    int ans_max = W / A;
    if (ans_min > ans_max)
    {
        cout << "UNSATISFIABLE\n";
    }
    else
    {
        cout << ans_min << " " << ans_max << endl;
    }

    return 0;
}