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
    rep(i, N)
    {
        cin >> A[i];
    }
    // 被っている漫画を一時退避するベクトル
    vector<int> kaburi;
    // 被っている漫画は後ろに入れて、交換時に後ろから取り出すためdequeを使う
    deque<int> manga;
    sort(A.begin(), A.end());
    rep(i, N)
    {
        if (i != 0 && A[i] == A[i - 1])
        {
            kaburi.push_back(A[i]);
        }
        else
        {
            manga.push_back(A[i]);
        }
    }
    rep(i, kaburi.size())
    {
        manga.push_back(kaburi[i]);
    }
    int ans = 0;
    while (!manga.empty())
    {
        int c = manga.front();
        if (c != ans + 1)
        {
            if (manga.size() >= 2)
            {
                manga.pop_back();
                manga.pop_back();
                ans++;
            }
            else
            {
                break;
            }
        }
        else
        {
            manga.pop_front();
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}