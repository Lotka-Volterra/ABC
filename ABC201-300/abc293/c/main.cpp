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
    int H, W;
    cin >> H >> W;
    vector<vector<int>> A(H, vector<int>(W));
    rep(i, H)
    {
        rep(j, W)
        {
            cin >> A[i][j];
        }
    }
    vector<char> Route;
    // Dなら↓、Rなら→
    rep(i, H - 1)
    {
        Route.push_back('D');
    }
    rep(i, W - 1)
    {
        Route.push_back('R');
    }
    sort(Route.begin(), Route.end());
    int ans = 0;
    do
    {
        set<int> S;
        S.insert(A[0][0]);
        int h = 0, w = 0;
        for (int i = 0; i < Route.size(); i++)
        {

            if (Route[i] == 'D')
            {
                h++;
            }
            else
            {
                w++;
            }
            S.insert(A[h][w]);
        }
        if (S.size() == H + W - 1)
        {
            ans++;
        }
    } while (next_permutation(Route.begin(), Route.end()));
    cout << ans << endl;
    return 0;
}