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
    ll N, Q;
    cin >> N >> Q;
    vector<ll> A(N), minusA(N);
    rep(i, N)
    {
        ll a;
        cin >> a;
        A[i] = a;
        minusA[i] = -a;
    }
    sort(A.begin(), A.end());
    sort(minusA.begin(), minusA.end());

    vector<ll> sumA(N), minusSumA(N);
    sumA[0] = A[0];
    minusSumA[0] = minusA[0];
    for (int i = 1; i < N; i++)
    {
        sumA[i] = sumA[i - 1] + A[i];
        minusSumA[i] = minusSumA[i - 1] + minusA[i];
    }

    rep(i, Q)
    {
        ll x;
        cin >> x;
        auto itr1 = lower_bound(A.begin(), A.end(), x);
        auto itr2 = lower_bound(minusA.begin(), minusA.end(), -x);

        ll ans = 0;
        if (itr1 == A.end() || itr1 == A.begin() || itr2 == minusA.begin())
        {
            ans = abs(N * x - sumA[N - 1]);
        }
        else
        {
            ll index1 = itr1 - A.begin();
            ans = abs(sumA[index1 - 1] - x * (index1));
            ll index2 = itr2 - minusA.begin();
            ans += abs(-minusSumA[index2 - 1] - x * (index2));
        }
        cout << ans << endl;
    }
    return 0;
}