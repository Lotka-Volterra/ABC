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
    int N, M, H, K;
    string S;
    cin >> N >> M >> H >> K >> S;
    map<int, vector<int>> dict;
    int X, Y;
    rep(i, M)
    {
        cin >> X >> Y;
        dict[X].push_back(Y);
    }
    int pos_x, pos_y;
    pos_x = 0;
    pos_y = 0;

    rep(i, N)
    {
        if (S[i] == 'L')
        {
            pos_x--;
        }
        else if (S[i] == 'R')
        {
            pos_x++;
        }
        else if (S[i] == 'U')
        {
            pos_y++;
        }
        else
        {
            pos_y--;
        }
        H--;
        if (H < 0)
        {
            No;
            return 0;
        }
        vector<int>::iterator itr = find(dict[pos_x].begin(), dict[pos_x].end(), pos_y);
        if (itr != dict[pos_x].end() && H < K)
        {
            H = K;
            auto new_end = remove(dict[pos_x].begin(), dict[pos_x].end(), pos_y);

            // 実際にベクタから要素を削除する
            dict[pos_x].erase(new_end, dict[pos_x].end());
        }
    }
    Yes;
}