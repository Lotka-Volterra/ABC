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
    int n;
    cin >> n;
    int count = 0;
    vector<int> ans;
    rep(a, 4)
    {
        rep2(b, a, 4)
        {
            rep2(c, b, 4)
            {
                rep2(d, c, 4)
                {
                    rep2(e, d, 4)
                    {
                        rep2(f, e, 4)
                        {
                            rep2(g, f, 4)
                            {
                                rep2(h, g, 4)
                                {
                                    rep2(i, h, 4)
                                    {
                                        rep2(j, i, 4)
                                        {
                                            rep2(k, j, 4)
                                            {
                                                rep2(l, k, 4)
                                                {
                                                    count++;
                                                    if (count == n)
                                                    {
                                                        ll num = 0;
                                                        num = pow(10, 12) * a + pow(10, 11) * b + pow(10, 10) * c + pow(10, 9) * d + pow(10, 8) * e + pow(10, 7) * f + pow(10, 6) * g + pow(10, 5) * h + pow(10, 4) * i + pow(10, 3) * j + pow(10, 2) * k + 10 * l + 3;
                                                        cout << num << endl;
                                                        return 0;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return 0;
}