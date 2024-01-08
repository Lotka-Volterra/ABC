# 備忘録
# 入力が何行続くかわからない場合、無限ループで受け取り、EOFErrorで無限ループを抜ける
ans = set()
while True:
    try:
        s = input().split()
    except EOFError:
        break

    for char in s:
        if char[0].isupper() or char[0].isdigit():
            ans.add(char)
print(len(ans))
