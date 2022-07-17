w, h = map(int, input().split())
if (w//4)*3 == h:
    print("4:3")
else:
    print("16:9")

#割り算を考えなくて良いようにするには、比の考え方を使う
if 3*w == 4*h:
    print("4:3")
else:
    print("16:9")
#別解　最大公約数（GCD）を求めて割る（４と３、16と９は互いに素なのでこの比になる）