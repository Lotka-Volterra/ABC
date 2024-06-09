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

    int N, Q;
    cin >> N >> Q;
    vector<pair<int, int>> A(N, {0, 0});
    rep(i, N)
    {
        A[i].first = i + 1;
    }
    int x = 1, y = 0;
    reverse(A.begin(), A.end());
    rep(i, Q)
    {
        int q1;
        cin >> q1;
        if (q1 == 1)
        {
            string q2;
            cin >> q2;
            if (q2 == "L")
            {
                x -= 1;
            }
            else if (q2 == "R")
            {
                x += 1;
            }
            else if (q2 == "U")
            {
                y += 1;
            }
            else
            {
                y -= 1;
            }
            A.push_back({x, y});
        }
        else
        {
            int q2;
            cin >> q2;
            cout << A[A.size() - q2].first << " " << A[A.size() - q2].second << endl;
        }
    }
    return 0;
}