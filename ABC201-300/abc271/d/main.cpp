#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
    int N, S;
    cin >> N >> S;

    vector<int> A(N), B(N);

    // 入力の受け取りと合計Sの計算
    for (int i = 0; i < N; i++)
    {
        cin >> A[i] >> B[i];
    }

    // DP配列の初期化
    vector DP(N + 1, vector<string>(S + 1, ""));
    DP[1][A[0]] = "H";
    DP[1][B[0]] = "T";

    for (int i = 1; i < N; i++)
    {
        for (int j = S; j >= 0; j--)
        {
            if (DP[i][j] == "")
            {
                continue;
            }

            if (j + A[i] <= S)
            {

                DP[i + 1][j + A[i]] = DP[i][j] + "H";
            }
            if (j + B[i] <= S)
            {
                DP[i + 1][j + B[i]] = DP[i][j] + "T";
            }
        }
    }

    if (DP[N][S] != "")
    {
        cout << "Yes" << endl;
        cout << DP[N][S] << endl;
    }
    else
    {
        cout << "No" << endl;
    }
    return 0;
}
