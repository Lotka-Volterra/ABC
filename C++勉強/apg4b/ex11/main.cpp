#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, A, B;
    string op;
    cin >> N >> A;
    rep(i, N)
    {
        cin >> op >> B;
        if (op == "+")
        {
            A += B;
        }
        else if (op == "-")
        {
            A -= B;
        }
        else if (op == "*")
        {
            A *= B;
        }
        else if (op == "/" && B != 0)
        {
            A /= B;
        }
        else
        {
            cout << "error" << endl;
            break;
        }
        cout << i + 1 << ":" << A << endl;
    }
    return 0;
}