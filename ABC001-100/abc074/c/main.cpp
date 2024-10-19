#include <bits/stdc++.h>
using namespace std;

// https://qiita.com/drken/items/97e37dd6143e33a64c8c
// index が条件を満たすかどうか
vector<int> sugar;
int A, B, C, D, E, F;

bool isOK(int index, int water)
{
    // 質量チェック
    if (water - sugar[index] > F)
    {
        return false;
    }
    // 濃度チェック
    if ((100 + E) * (-sugar[index]) > E * (water - sugar[index]))
        return false;

    return true;
}

// 汎用的な二分探索のテンプレ
int binary_search(int water)
{
    // ngは条件を満たさないインデックスの最大値
    int ng = -1; // 「index = 0」が条件を満たすこともあるので、初期値は -1
    // okは条件を満たすインデックスの最小値
    int ok = (int)sugar.size() - 1; // 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    // ok と ng のどちらが大きいかわからないことを考慮
    // (ng,ok]と[ok,ng)の両方に対応できる
    while (abs(ok - ng) > 1)
    {
        int mid = (ok + ng) / 2;

        if (isOK(mid, water))
            ok = mid;
        else
            ng = mid;
    }
    return ok;
}

int main()
{
    cin >> A >> B >> C >> D >> E >> F;
    for (int i = 0; i < 3001; ++i)
    {
        for (int j = 0; j < 3001; j++)
        {
            int s = C * i + D * j;
            if (s <= F)
            {
                sugar.push_back(-s);
            }
        }
    }
    sort(sugar.begin(), sugar.end());
    double ans = -1;
    int ans_s = 0, ans_w = 0;
    for (int i = 0; i < 3001; i++)
    {
        for (int j = 0; j < 3001; j++)
        {
            int water = (A * i + B * j) * 100;
            if (water > F || water == 0)
            {
                break;
            }
            int ok = binary_search(water);
            double noudo = (double)100 * (-sugar[ok]) / (water - sugar[ok]);
            if (noudo > ans)
            {
                ans = noudo;
                ans_s = -sugar[ok];
                ans_w = water;
            }
        }
    }
    cout << ans_w + ans_s << " " << ans_s << endl;
    return 0;
}
