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
    auto S = vector<char>(7);
    string s;
    cin >> s;
    rep(i, 7)
    {
        S[i] = s[i];
    }
    map<char, int> dict;
    rep(i, 7)
    {
        dict[S[i]] = i;
    }
    string ans_string = "atcoder";
    // map<char, int> ans_dict;
    // rep(i, 7)
    // {
    //     ans_dict[ans_string[i]] = i;
    // }
    int ans = 0;
    rep(i, 7)
    {
        while (dict[ans_string[i]] != i)
        {
            int wrong_index = dict[ans_string[i]];
            if (wrong_index > i)
            {
                dict[S[wrong_index]] = wrong_index - 1;
                dict[S[wrong_index - 1]] = wrong_index;
                S[wrong_index] = S[wrong_index - 1];
                S[wrong_index - 1] = ans_string[i];
                wrong_index--;
            }
            else
            {
                dict[S[wrong_index]] = wrong_index + 1;
                dict[S[wrong_index + 1]] = wrong_index;
                S[wrong_index] = S[wrong_index + 1];
                S[wrong_index + 1] = ans_string[i];
                wrong_index++;
            }
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}