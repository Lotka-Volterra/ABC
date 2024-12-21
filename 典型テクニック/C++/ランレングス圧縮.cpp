#include <bits/stdc++.h>
using namespace std;

using ll = long long;
vector<pair<char, ll>> runLengthEncoding(string s)
{
    vector<pair<char, ll>> res;
    ll cnt = 1;
    char pre = s[0];
    for (int i = 1; i < (int)s.length(); ++i)
    {
        if (pre != s[i])
        {
            res.push_back({pre, cnt});
            pre = s[i];
            cnt = 1;
        }
        else
            cnt++;
    }
    res.push_back({pre, cnt});
    return res;
}

int main()
{
    string S;
    cin >> S;
    auto blocks = runLengthEncoding(S);
}
