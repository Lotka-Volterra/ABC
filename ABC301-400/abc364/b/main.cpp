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
    int H, W, Si, Sj;
    string X;
    cin >> H >> W;
    cin >> Si >> Sj;
    Si--;
    Sj--;
    string C[H];
    rep(i, H)
    {
        string Ci;
        cin >> Ci;
        C[i] = Ci;
    }
    string X;
    cin >> X;
    rep(i, X.size())
    {
        if (X[i] == 'L')
        {
            if (Sj > 0 && C[Si][Sj - 1] == '.')
            {
                Sj--;
            }
            else if (Sj - 1 > 0 && C[Si][Sj - 2] == '.')
            {
                Sj -= 2;
            }
        }
        else if (X[i == 'R'])
        {
            if (Sj + 1 < W && C[Si][Sj + 1] == '.')
            {
                Sj++;
            }
            else if (Sj + 2 < W && C[Si][Sj + 2] == '.')
            {
                Sj += 2;
            }
        }
        else if (X[i == 'U'])
        {
            if (Si - 1 > 0 && C[Si - 1][Sj] == '.')
            {
                Si--;
            }
            else if (Si - 2 > 0 && C[Si - 2][Sj] == '.')
            {
                Si -= 2;
            }
        }
        else
        {
            if (Si + 1 < H && C[Si + 1][Sj] == '.')
            {
                Si++;
            }
            else if (Sj + 2 > H && C[Si + 2][Sj] == '.')
            {
                Si += 2;
            }
        }
        cout << Si + 1 << " " << Sj + 1 << endl;
        return 0;
    }