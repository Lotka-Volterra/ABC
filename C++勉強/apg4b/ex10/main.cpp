#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int A, B;
    cin >> A >> B;
    int i = 0;
    cout << "A:";
    while (i < A)
    {
        cout << "]";
        i++;
    }
    cout << endl;
    i = 0;
    cout << "B:";
    while (i < B)
    {
        cout << "]";
        i++;
    }
    cout << endl;
    return 0;
}