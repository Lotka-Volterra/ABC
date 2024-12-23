#include <bits/stdc++.h>
using namespace std;

using ll = long long;
vector<ll> a = {1, 14, 32, 51, 51, 51, 243, 419, 750, 910};
// https://qiita.com/drken/items/97e37dd6143e33a64c8c
// index が条件を満たすかどうか
bool isOK(ll index, ll key)
{
    if (a[index] >= key) //
        return true;
    else
        return false;
}

// 汎用的な二分探索のテンプレ
ll binary_search(ll key)
{
    // ngは条件を満たさないインデックスの最大値
    ll ng = -1L; // 「index = 0」が条件を満たすこともあるので、初期値は -1
    // okは条件を満たすインデックスの最小値
    ll ok = (ll)a.size(); // 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    // ok と ng のどちらが大きいかわからないことを考慮
    // (ng,ok]と[ok,ng)の両方に対応できる
    while (abs(ok - ng) > 1)
    {
        ll mid = (ok + ng) / 2;

        if (isOK(mid, key))
            ok = mid;
        else
            ng = mid;
    }
    return ok;
}

int main()
{
    cout << binary_search(51) << endl;  // a[3] = 51
    cout << binary_search(1) << endl;   // a[0] = 1
    cout << binary_search(910) << endl; // a[9] = 910

    cout << binary_search(52) << endl;  // 6
    cout << binary_search(0) << endl;   // 0
    cout << binary_search(911) << endl; // 10 (場外)
}
