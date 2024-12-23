#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// ABC204D kanpurinさんの回答をC++で書き直し
// いくつかを選んでその和をなるべくS/2に近づけることが方針。
// 一次元配列でDPしているのが、個人的に驚きだったのでメモ。
using ll = long long;

int main()
{
    int N;
    cin >> N;

    vector<int> T(N);
    int S = 0;

    // 入力の受け取りと合計Sの計算
    for (int i = 0; i < N; i++)
    {
        cin >> T[i];
        S += T[i];
    }

    // DP配列の初期化
    vector<bool> DP(S / 2 + 1, false);
    DP[0] = true; // 初期状態として、0は常に選べる

    // DPの処理
    for (int i = 0; i < N; i++)
    {
        // 遷移を逆順に行うことで、1つのT[i]に対して遷移が行われた結果を、同じステップ中で二度適用しない
        // 一次元なので、DPの配列を使い回す都合上、以前のループで行われた遷移かどうかを判別できない
        // つまり、正順で遷移を行うと、dp[i]をもとにdp[i+1]を更新。更新されたdp[i+1]をもとにdp[i+2]を更新するというような、
        // 一つのT[i]でdp[i]から2回以上遷移が行われるというような事態が起きてしまう。
        // そのため、逆順に遷移を行っている。
        // また、最終的な答えはS/2付近にあるので、jの開始地点もS/2からにして、全探索していない。
        for (int j = S / 2; j >= T[i]; j--)
        {
            DP[j] = DP[j] || DP[j - T[i]];
        }
    }

    // S/2に最も近い部分和を探す
    // S/2までで、DP[i]=trueになるもの(実現できる部分和)を探す。昇順に探索するので、max_sumは部分和が存在するiで更新され続ける
    int max_sum = 0;
    for (int i = 0; i <= S / 2; i++)
    {
        if (DP[i])
        {
            max_sum = i;
        }
    }

    // 結果を出力
    // ここまでで求めたのは、部分和を0から最もS/2に近づける方法(2つのオーブンの使用時間のうち、短い方。)
    // 求めるのは、使用時間が長い方なので、Sから引く
    cout << S - max_sum << endl;

    return 0;
}
