#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // 30は素因数として2,3,5をもつ。
    // 交差を30とする数列、たとえば数列30*k+1は初項も交差も小さな素因数を避けることができるので、素数の出現率が高く見える数列である。
    // どんな素数でもいいので数個から数十個の素数が欲しい、というときに使えるかもしれない
    // 下記は30*k+1で表される数列を素数の候補を出すために使っている
    // ABC096D editorial模範解答
    // https://atcoder.jp/contests/abc096/submissions/2444746
    return 0;
}