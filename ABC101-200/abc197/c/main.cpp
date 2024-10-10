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
    int N;
    cin >> N;
    vector<int> A(N);
    int ans = 1 << 30;
    rep(i, N)
    {
        cin >> A[i];
    }
    bool Answer = false;
    rep(i, 1 << (N - 1)) // i=0から1<<N-2まで全探索
    {
        vector<int> ORlist;
        int firstOR = A[0];
        rep(j, N - 1)
        {
            // OR演算の起点
            firstOR |= A[j];
            if (i & (1 << j)) // iと1<<jでAND演算。iの下からj桁目が2進数表記で1なら、真（非ゼロ）を返す
            {
                ORlist.push_back(firstOR);
                firstOR = A[j + 1];
            }
        }
        // 最後の要素をOR演算してORリストに追加
        firstOR |= A[N - 1];
        ORlist.push_back(firstOR);
        int firstXOR = ORlist[0];
        for (int j = 1; j < ORlist.size(); j++)
        {
            firstXOR ^= ORlist[j];
        }
        ans = min(ans, firstXOR);
    }
    cout << ans << endl;
    return 0;
}