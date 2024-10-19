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
    int N, M;
    cin >> N >> M;
    set<int> A;
    rep(i, N)
    {
        int a;
        cin >> a;
        A.insert(a);
    }
    set<int> Ans;
    for (int i = 1; i <= M; i++)
    {
        Ans.insert(i);
    }
    for (auto it = A.begin(); it != A.end(); it++)
    {
        int ai = *it;
        for (int i = 2; i * i <= ai; ++i)
        {
            if (ai % i == 0)
            {
                // 約数の倍数を削除→素因数が残る
                if (Ans.find(i) != Ans.end()) // その要素がもう削除されている場合、その要素の倍数も削除済みのため処理は行わない
                {
                    for (int j = i; j <= M; j += i)
                    {
                        Ans.erase(j);
                    }
                }

                int k = ai / i;
                // もう一つの約数の倍数を削除→素因数が残る
                if (Ans.find(k) != Ans.end()) // その要素がもう削除されている場合、その要素の倍数も削除済みのため処理は行わない
                {
                    for (int j = k; j <= M; j += k)
                    {
                        Ans.erase(j);
                    }
                }
            }
        }
        if (ai != 1)
        {
            // aiが素数の場合を考慮して、ai自体の倍数を削除
            for (int i = ai; i <= M; i += ai)
            {
                Ans.erase(i);
            }
        }
    }
    cout << Ans.size() << endl;
    for (auto it = Ans.begin(); it != Ans.end(); it++)
    {
        cout << *it << endl;
    }

    return 0;
}