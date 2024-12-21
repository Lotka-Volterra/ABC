#include <bits/stdc++.h>

using namespace std;
int main()
{
    // リファクタ yuto1115さんのものを参考に理解できる範囲で
    const long long mod = 998244353LL; // 定数化
    int N;
    cin >> N;
    vector<vector<long long>> dp(N, vector<long long>(2, 0LL)); // pairではなくN*2の2次元配列にして要素にアクセスしやすくする
    dp[0][0] = 1LL;
    dp[0][1] = 1LL;

    vector cards(N, vector<int>(2)); // int型のNとvector<int>(2)から、cardsはvector<vector<int,int>>だと型推論される
    for (int i = 0; i < N; i++)
    {
        cin >> cards[i][0] >> cards[i][1]; //>>で繋いで入力も一行に
    }
    for (int i = 1; i < N; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                if (cards[i][j] != cards[i - 1][k]) // 4つのif文を、1つに
                {
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % mod;
                }
            }
        }
    }
    cout << (dp[N - 1][0] + dp[N - 1][1]) % mod << endl;
    return 0;
}
