#include <bits/stdc++.h>

using namespace std;
// 模範解答を解釈、改造
int main()
{
    int n, q;
    cin >> n >> q;
    vector<long long> a(n);
    for (auto &nx : a)
    {
        cin >> nx;
    }
    sort(a.begin(), a.end());

    vector<long long> rw(n + 1, 0); // 累積和
    for (long long i = 0; i < n; i++)
    {
        rw[i + 1] = rw[i] + a[i]; // rw[0]=0,rw[1]=a[0]
    }

    for (int i = 0; i < q; i++)
    {
        long long x;
        cin >> x;
        // upper_boundだが、fiをn-1に設定することで、a.end()になることがない
        // st>fi(実際はfi+1=st)になれば終わり
        int st = 0, fi = n - 1;
        while (st <= fi)
        {
            int te = (st + fi) / 2;
            if (a[te] < x)
            {
                st = te + 1;
            }
            else
            {
                fi = te - 1;
            }
        }
        // cout << st << " " << fi << endl;
        // st=fiになったループを考える
        // a[0]=>xならst=0,fi=-1
        // a[n-1]<xならst=n,fi=n-1
        // 0<k<=n-1でa[k]=>xならst=k,fi=k-1
        // つまりk-1までa[i]<xで、kからa[i]=>x
        // rwは1-indexedであることに注意する。a[k-1]までの累積和はrw[k]
        // x*(k-1)-rw[k]+(rw[n]-rw[k+1])-x*(n-(k-1))
        long long res = x * st; // fi,stは0-indexedなので、k-1個を表すにはfiではなくstを使う
        // res -= rw[fi + 1];
        // res += (rw[n] - rw[st]);
        // res -= x * (n - st);
        res -= rw[st];
        res += (rw[n] - rw[st]); // kからn-1までの累積和。1-indexedにすると、nまでの累積和からkまでの累積和を引くこと
        res -= x * (n - st);     // fi,stは0-indexedなので、n-(k-1)個を表すにはn-stを使う
        cout << res << '\n';
    }
    return 0;
}
