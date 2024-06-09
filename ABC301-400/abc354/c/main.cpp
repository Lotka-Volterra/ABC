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
    int N, A, C;
    cin >> N;
    vector<array<int, 3>> AC(N);
    rep(i, N)
    {
        cin >> A >> C;
        AC[i] = {A, -C, i};
    }
    // 弱い＊コストが高い順に並べる
    sort(AC.begin(), AC.end());
    vector<int> Ans;
    // 直後の要素（自分より強い）よりコストが安ければセーフ
    rep(i, N - 1)
    {
        if (AC[i][1] <= AC[i + 1][1])
        {
            Ans.push_back(AC[i][2]);
        }
        // 最後の要素を入れる
        Ans.push_back(AC[N - 1][2]);
        cout << Ans.size() << endl;
        rep(i, Ans.size())
        {
            if (i != Ans.size() - 1)
            {
                printf("%d ", Ans[i]);
            }
            else
            {
                printf("%d\n");
            }
        }
    }
    return 0;
}