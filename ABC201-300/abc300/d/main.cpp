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
    ll n;
    cin >> n;
    ll ans = 0LL;
    vector<ll> primes;
    for (int i = 2; i < 4e5 + 1; i++)
    {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++)
        {
            if (i % j == 0)
            {
                isPrime = false;
            }
        }
        if (isPrime)
        {
            primes.push_back((ll)i);
        }
    }
    int s = (int)primes.size();
    for (int a = 0; a < s - 2; a++)
    {
        if (primes[a] > 1e3)
        {
            break;
        }

        for (int b = a + 1; b < s - 1; b++)
        {
            if (primes[b] > 1e4)
            {
                break;
            }
            for (int c = b + 1; c < s; c++)
            {
                if (primes[a] * primes[a] * primes[b] * primes[c] * primes[c] <= n)
                {
                    ans++;
                }
                else
                {
                    break;
                }
            }
        }
    }

    cout << ans << endl;
    return 0;
}