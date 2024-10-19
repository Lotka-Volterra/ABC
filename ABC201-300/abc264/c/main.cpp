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
    ll H1, W1, H2, W2;
    cin >> H1 >> W1;
    vector<vector<int>> A(H1, vector<int>(W1));
    vector<vector<int>> B(H2, vector<int>(W2));

    rep(i, H1)
    {
        rep(j, W1)
        {
            cin >> A[i][j];
        }
    }
    cin >> H2 >> W2;

    rep(i, H2)
    {
        rep(j, W2)
        {
            cin >> B[i][j];
        }
    }
    // 0からH1までの数をベクトルに格納
    vector<int> nums;
    for (int i = 0; i < H1; ++i)
    {
        nums.push_back(i);
    }

    ll diffH = H1 - H2;
    ll diffW = W1 - W2;
    // diffH個を選ぶ組み合わせのためのビットマスクを作成
    vector<bool> selectorH(H1, false); // H1個のうちdiffH個をtrueにする
    fill(selectorH.begin(), selectorH.begin() + diffH, true);
    vector<bool> selectorW(W1, false); // H1個のうちdiffH個をtrueにする
    fill(selectorW.begin(), selectorW.begin() + diffW, true);
    // next_permutationで全ての組み合わせを列挙
    do
    {
        do
        {
            vector<vector<int>> newA(H2, vector<int>(W2));
            int indexI = 0, indexJ = 0;
            for (int i = 0; i < H1; ++i)
            {
                if (selectorH[i])
                {
                    continue;
                }
                for (int j = 0; j < W1; ++j)
                {
                    if (selectorW[j])
                    {
                        continue;
                    }
                    newA[indexI][indexJ] = A[i][j];
                    indexJ++;
                }

                indexI++;
            }
            bool same = true;
            rep(i, H2)
            {
                rep(j, W2)
                {
                    if (newA[i][j] != B[i][j])
                    {
                        same = false;
                        break;
                    }
                }
            }
            if (same)
            {
                Yes;
                return 0;
            }
        } while (prev_permutation(selectorW.begin(), selectorW.end()));
    } while (prev_permutation(selectorH.begin(), selectorH.end()));
    No;
    return 0;
}