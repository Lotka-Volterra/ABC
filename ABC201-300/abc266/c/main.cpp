#include <iostream>

using namespace std;

int dotProduct(int x1, int y1, int x2, int y2)
{
    return x1 * y1 + y2 * x2;
}

int main()
{
    int ax, ay, bx, by, cx, cy, dx, dy;
    cin >> ax >> ay >> bx >> by >> cx >> cy >> dx >> dy;

    int ab1 = ax - bx;
    int ab2 = ay - by;
    int cb1 = cx - bx;
    int cb2 = cy - by;

    int cp1 = dotProduct(ab1, ab2, cb1, cb2);

    int bc1 = bx - cx;
    int bc2 = by - cy;
    int dc1 = dx - cx;
    int dc2 = dy - cy;

    int cp2 = dotProduct(bc1, bc2, dc1, dc2);

    int cd1 = cx - dx;
    int cd2 = cy - dy;
    int ad1 = ax - dx;
    int ad2 = ay - dy;

    int cp3 = dotProduct(cd1, cd2, ad1, ad2);

    int da1 = dx - ax;
    int da2 = dy - ay;
    int ba1 = bx - ax;
    int ba2 = by - ay;

    int cp4 = dotProduct(da1, da2, ba1, ba2);
    cout << cp1 << cp2 << cp3 << cp4 << endl;
    if (cp1 > 0 && cp2 > 0 && cp3 > 0 && cp4 > 0)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
    return 0;
}
