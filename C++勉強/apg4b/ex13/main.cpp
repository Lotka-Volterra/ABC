#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
// using namespace atcoder;
using ll = long long;
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<int> vec(N);
    int average = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> vec.at(i);
        average += vec.at(i);
    }
    average /= N;

    for (int i = 0; i < N; i++)
    {
        cout << abs(vec.at(i) - average) << endl;
    }
    return 0;
}