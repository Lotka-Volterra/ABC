#include <bits/stdc++.h>
using namespace std;
using ll = long long;
// 初めてのE問題AC
int main()
{
    ll x;
    cin >> x;
    string stx = to_string(x);
    if (stx.size() <= 2)
    {
        cout << x << endl;
        return 0;
    }
    int nokori = stx.size() - 2;
    for (int i = stoi(stx.substr(0, 2)); i <= 111; i++)
    {
        string sti = to_string(i).substr(0, 2);
        string ans = sti.substr(0, 2);
        int nokoritemp = nokori;
        if (i >= 100)
        {
            nokoritemp++;
        }
        int diff = sti[1] - sti[0];
        if (diff >= 0 && diff * (nokoritemp) + (sti[1] - '0') > 9)
        {
            continue;
        }
        if (diff < 0 && diff * (nokoritemp) + (sti[1] - '0') < 0)
        {
            continue;
        }

        for (int i = 1; i <= nokoritemp; i++)
        {
            ans += to_string(sti[1] - '0' + diff * i);
        }
        if (ans < stx)
        {
            continue;
        }

        cout << ans << endl;
        return 0;
    }
    return 0;
}
