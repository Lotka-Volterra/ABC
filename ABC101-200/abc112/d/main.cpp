#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main()
{
    int N, M;
    cin >> N >> M;
    int ans = 1;
    for (int i = 2; i <= M / N; i++)
    {
        if ((M - i * (N - 1)) % i == 0)
        {
            ans = i;
        }
    }
    cout << ans << endl;
}
