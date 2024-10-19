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

    // グリッドを読み込んで #の位置の集合を返す
    vector<pair<int, int>> S;
    rep(y, N)
    {
        string s;
        cin >> s;
        rep(x, N)
        {
            if (s[x] == '#')
            {
                S.push_back({x, y});
            }
        }
    }
def read():
  S = set()
  for y in range(N):
    l = input()
    for x in range(N):
      if l[x]=="#":
        S.add((x, y))
  return S

S = read()
T = read()

for _ in range(4):
#最も左（複数あればそのうちで最も上）の #を(0, 0) の位置にする
  mx, my = min(S)
  S = set((x-mx, y-my) for x, y in S)
  mx, my = min(T)
  T = set((x-mx, y-my) for x, y in T)

  if S==T:
    print("Yes")
    exit(0)

#Tを回転
  T = set((y, -x) for x, y in T)

print("No")
}