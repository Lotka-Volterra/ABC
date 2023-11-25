a, b = input().split()
sa = int(a[0])+int(a[1])+int(a[2])
sb = int(b[0])+int(b[1])+int(b[2])
if sa >= sb:
    print(sa)
else:
    print(sb)
# 同じ値ならS(A)を出力する、というのに惑わされない。同じ値ならどっちでもいいから、maxを使えばいい
print(max(sa, sb))
