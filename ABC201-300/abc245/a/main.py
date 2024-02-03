a, b, c, d = map(int, input().split())
if a < c:
    print("Takahashi")
elif a == c and b <= d:
    print("Takahashi")
else:
    print("Aoki")
# X 時 Y 分は 0 時 0 分から 60X+Y 分経過しているので、 P=60A+B,Q=60C+D として P,Q の大小を比較する方針を取ると場合分けが少なく済みます
if 60*a+b<=60*c+d:
    print('Takahashi')
else:
    print('Aoki')