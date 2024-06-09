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
    string S, T;
    cin >> S >> T;
    auto alphS = vector<int>(26);
    auto alphT = vector<int>(26);
    int atS = 0, atT = 0;
    rep(i, S.size())
    {
        if (islower(S[i]))
        {
            alphS[S[i] - 'a']++;
        }
        else
        {
            atS++;
        }
        if (islower(T[i]))
        {
            alphT[T[i] - 'a']++;
        }
        else
        {
            atT++;
        }
    }
    set<int> excludedValues = {0, 2, 3, 4, 14, 17, 19};
    rep(i, 26)
    {
        if (alphS[i] == alphT[i])
        {
            continue;
        }
        else
        {
            // a,t,c,o,d,e,rのいずれかの箇所が異なる場合
            if (excludedValues.find(i) != excludedValues.end())
            {
                if (alphS[i] > alphT[i])
                {
                    if (atT >= alphS[i] - alphT[i])
                    {
                        atT -= alphS[i] - alphT[i];
                    }
                    else
                    {
                        No;
                        return 0;
                    }
                }
                else
                {
                    if (atS >= alphT[i] - alphS[i])
                    {
                        atS -= alphT[i] - alphS[i];
                    }
                    else
                    {
                        No;
                        return 0;
                    }
                }
            }
            else
            {
                No;
                return 0;
            }
        }
    }
    Yes;
    return 0;
}