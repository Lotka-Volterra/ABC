#include <bits/stdc++.h>

using namespace std;
// ABC264 C
// https://atcoder.jp/contests/abc264/editorial/4582
// https://scrapbox.io/pocala-kyopro/%E8%BB%A2%E5%80%92%E6%95%B0
// BITとは、一点加算、1~N番目までの区間和をどちらもlogで計算できる便利なデータ構造。転倒数の計算にも使う
// BITは1-indexed
vector<int> bit;
int sum(int i)
{
    int s = 0;
    while (i > 0)
    {
        s += bit[i];
        i -= i & (-i); // 次のインデックスに移る
    }
    return s;
}

void add(int i, int x)
{
    while (i < bit.size())
    {
        bit[i] += x;
        i += i & (-i);
    }
}

int main()
{
    bit.resize(10);
    for (int i = 0; i < 10; i++)
    {
        bit[i] = 0;
    }

    string s;
    cin >> s;
    map<char, int> mp;
    string atc = "*atcoder";
    // atcoderは全ての文字が互いに異なるので、mapで位置を対応付けられる(1-indexed)
    for (int i = 1; i <= 7; i++)
    {
        mp[atc[i]] = i;
    }
    vector<int> a = {-1};
    // 入力された文字列の文字の順番に、atcoderにおける位置をaに格納
    // 例:catoderなら、aは初期値の-1を含めると、{-1,3,1,2,4,5,6,7}
    for (int i = 0; i < 7; i++)
    {
        a.push_back(mp[s[i]]);
    }

    int res = 0;
    for (int i = 1; i <= 7; i++)
    {
        res += (i - 1 - sum(a[i]));
        add(a[i], 1);
    }
    cout << res << "\n";
    return 0;
}
