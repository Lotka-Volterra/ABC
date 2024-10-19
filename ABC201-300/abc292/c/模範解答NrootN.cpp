#include <bits/stdc++.h>
using namespace std;

int main()
{

    int N;
    cin >> N;

    long long ans = 0;

    for (int i = 1; i < N; i++)
    {
        // 一方をA*B=Xと仮定すると、もう一方のC*D=N-X
        int X = i, Y = N - i;
        long long x = 0, y = 0;
        for (int j = 1; j * j <= X; j++)
        {
            if (X % j == 0)
            {
                x++;
                // X!=j*jなら、X/jはjと異なる。今回A<=Bを仮定しているので、A>Bの場合を同時に考慮してさらに1増やす
                if (X != j * j)
                    x++;
            }
        }
        for (int j = 1; j * j <= Y; j++)
        {
            if (Y % j == 0)
            {
                y++;
                if (Y != j * j)
                    y++;
            }
        }
        ans += x * y;
    }

    cout << ans << endl;

    return 0;
}
