#include <bits/stdc++.h>

using namespace std;
#define MAXP 1000005
// https://atcoder.jp/contests/abc250/editorial/3896
vector<long long> prime_list;
void construct_plist()
{
    vector<bool> fl(MAXP, false);
    for (int i = 2; i < MAXP; i++)
    {
        if (fl[i])
        {
            continue;
        }
        prime_list.push_back(i);
        for (int j = i; j < MAXP; j += i)
        {
            fl[j] = true;
        }
    }
}
// 64bitで収まらない可能性がある場合の扱い方
// 64bit(2**64、だいたい10**19)で収まらない場合、一旦doubleで計算して、収まらなかったら4e18(4**18=4*10**18を返す)
long long f(long long p, long long q)
{
    double est = 1;
    est = (q * q * q);
    est *= p;
    if (est > 4e18)
    {
        return 4e18;
    }
    return p * q * q * q;
}

int main()
{
    construct_plist();
    long long n;
    cin >> n;
    long long res = 0;
    int sz = prime_list.size();
    int q = sz - 1;
    for (int p = 0; p < sz; p++)
    {
        while (p < q && f(prime_list[p], prime_list[q]) > n)
        {
            q--;
        }
        if (p >= q)
        {
            break;
        }
        res += (q - p);
    }
    cout << res << '\n';
    return 0;
}
// https://atcoder.jp/contests/abc180/editorial/1172
// 別の方法。多倍長整数を使う
// cpp_intをincludeして使う。intやlong long同様に扱える
// #include<bits/stdc++.h>
// using namespace std;

// #include<boost/multiprecision/cpp_int.hpp>
// using namespace boost::multiprecision;

// int main(){
//   cpp_int x,y,a,b;
//   cin>>x>>y>>a>>b;
//   cpp_int ans=0;

//   while(true){
//     //x*aが10**27程度になるが問題ない
//     if(x*a>x+b||x*a>=y){
//       break;
//     }
//     x*=a;
//     ans++;
//   }

//   ans+=(y-1-x)/b;
//   cout<<ans<<endl;
// }
