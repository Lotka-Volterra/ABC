A,B,C,D,E,F,X = list(map(int, input().split()))
#A秒とC秒を一セットにする。TSは商、TAは余り
TS = X // (A+C)
TA = X %(A+C)
#TAがAより大きい＝余りがAより大きいなら、A秒間すべて進めるので、TAをAに修正
if TA > A:
    TA = A
#商のセット分＊A秒と、余りの秒だけ秒速Bで進める
Taka = TS*A*B + TA*B

#同様
AS = X //(D+F)
AA = X % (D+F)
if AA > D:
    AA = D
Ao = AS*D*E + AA*E

#判定
if Taka > Ao:
    print("Takahashi")
elif Ao > Taka:
    print('Aoki')
else:
    print("Draw")