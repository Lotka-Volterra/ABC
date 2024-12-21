#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;

        ll p = 0, q = 0;
        for (ll i = 2; i * i * i <= n; i++) // min(p,q)<=nより、i*i*i<=n;
        {
            if (n % i != 0)
                continue;
            if ((n / i) % i == 0)
            {
                p = i;
                q = n / i / i;
            }
            else
            {
                q = i;
                p = (ll)sqrt(n / i);
            }
            break; // ここまで到達している時点でn%i==0。初めてn%i==0になる、最小のiの時に実行される。
        }
        cout << p << ' ' << q << endl;
    }
}
