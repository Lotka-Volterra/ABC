#include <bits/stdc++.h>
using namespace std;
// https://atcoder.jp/contests/abc276/submissions/36115419
// ABC276 C
// prev_permutaionは、ある順列について辞書順で一つ前の順列を生成する。
// 戻り値としては、前の順列が存在するかどうか(存在するならtrue)を返す

int main()
{
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> p[i];
    }
    prev_permutation(begin(p), end(p));
    for (int i = 0; i < n; ++i)
    {
        cout << p[i] << " \n"[i + 1 == n];
    }
    return 0;
}