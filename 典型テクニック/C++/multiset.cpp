#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
int main()
{
    // ABC253 C multiset
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q;
    cin >> Q;
    multiset<int> st;
    for (int i = 0; i < Q; i++)
    {
        int type;
        cin >> type;
        if (type == 1)
        {
            int x;
            cin >> x;
            st.insert(x);
        }
        else if (type == 2)
        {
            int x, c;
            cin >> x >> c;
            // st.erase(x)だと、存在するxを全て消してしまうので、For文で1回ずつ消す。
            // 1回ずつ消しても、プログラム全体の処理として最大Q回(挿入した以上の数を消すことはできない)
            for (int i = 0; i < c; i++)
            {
                auto itr = st.find(x);

                if (itr == st.end())
                {
                    break;
                }
                else
                {
                    st.erase(itr);
                }
            }
        }
        else
        {
            // multisetは小さい順で並んでいる。beginで開始(=最小値), rbeginはreverse begin(逆順の最小値=最大値)
            // beginやrbeginはO(1)つまり定数時間
            cout << *st.rbegin() - *st.begin() << endl;
        }
    }
    return 0;
}