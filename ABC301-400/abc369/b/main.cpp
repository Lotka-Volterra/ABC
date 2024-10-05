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
    int N;
    cin >> N;
    auto left = vector<int>();
    auto right = vector<int>();
    // int l = 0, r = 0;
    rep(i, N)
    {
        int A;
        char S;
        cin >> A >> S;
        if (S == 'L')
        {
            left.push_back(A);
        }
        else
        {
            right.push_back(A);
        }
    }
    // if (left.size() > 0)
    // {
    //     l = left[0];
    // }
    // if (right.size() > 0)
    // {
    //     r = right[0];
    // }
    int ans = 0;
    // 右手、左手は最初に出てくる鍵盤に置く。
    rep(i, left.size())
    {
        if (i != 0)
        {
            ans += abs(left[i] - left[i - 1]);
        }
    }
    rep(i, right.size())
    {
        if (i != 0)
        {
            ans += abs(right[i] - right[i - 1]);
        }
    }
    cout << ans << endl;
    return 0;
}