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
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    for (int i = A; i <= B; i++)
    {
        bool canBePrime = false;
        for (int j = C; j <= D; j++)
        {
            int num = i + j;
            // numが素数かどうか
            bool isPrime = true;
            for (int k = 2; k * k <= num; k++)
            {
                if (num % k == 0)
                {
                    isPrime = false;
                }
            }
            // 素数にできたなら、canBePrimeをtrueにする
            if (isPrime)
            {
                canBePrime = true;
            }
        }
        // iにたいして、どのようなjでも素数にできなかった場合、iを選ぶのが最適
        if (!canBePrime)
        {
            cout << "Takahashi" << endl;
            return 0;
        }
    }
    cout << "Aoki" << endl;
    return 0;
}