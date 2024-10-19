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
    vector<ll> T(N);
    vector<ll> X(N);
    vector<ll> A(N);

    rep(i, N)
    {
        cin >> T[i] >> X[i] >> A[i];
    }
    ll maxt = T[N - 1];
    vector<vector<ll>> Takahashi(maxt + 1, vector<ll>(5, -pow(10, 14)));
    Takahashi[0][0] = 0;
    int index = 0;
    for (int i = 1; i < maxt + 1; i++)
    {
        rep(j, 5)
        {
            ll score = 0;
            if (T[index] == i && j == X[index])
            {
                score = A[index];
                index++;
            }
            if (j != 0)
            {
                Takahashi[i][j] = Takahashi[i - 1][j - 1] + score;
            }
            if (j != 4)
            {
                Takahashi[i][j] = max(Takahashi[i][j], Takahashi[i - 1][j + 1] + score);
            }
            Takahashi[i][j] = max(Takahashi[i][j], Takahashi[i - 1][j] + score);
        }
    }
    ll ans = 0;
    rep(i, 5)
    {
        ans = max(ans, Takahashi[maxt][i]);
    }
    cout << ans << endl;
    return 0;
}