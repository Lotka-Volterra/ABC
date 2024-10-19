#include <bits/stdc++.h>

using namespace std;
// ABC264 C
// https://atcoder.jp/contests/abc264/editorial/4582
// 計算量は文字列の長さを |S|として O(|S|) 今回は7文字なので定数時間(入力によらず一定)
int main()
{
    string s;
    cin >> s;

    map<string, int> mp;
    queue<string> q;
    // 入力された文字列から、目的の文字列までの並び替え回数を保存するmap
    mp[s] = 0;
    // 入力された文字列を受け取って、キューに入れる
    // 幅優先探索を行う
    q.push(s);

    while (!q.empty())
    {
        string current = q.front();
        q.pop();
        // 目的の文字列になったら出力
        if (current == "atcoder")
        {
            cout << mp[current] << "\n";
            return 0;
        }
        // 今回、文字列は7文字
        for (int i = 1; i < 7; i++)
        {
            // nextを定義して、キューから取り出した文字列からi文字目とi-1文字目だけ入れ替える
            string next = current;
            swap(next[i - 1], next[i]);
            // 入れ替えた後のnextがmapに存在しないなら、キューとmapに追加。mapのバリューはcurrent+1(1文字さらに入れ替えたから)
            if (mp.find(next) == mp.end())
            {
                q.push(next);
                mp[next] = mp[current] + 1;
            }
        }
    }
    return 0;
}
