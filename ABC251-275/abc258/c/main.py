n, q = map(int, input().split())
s = input()
count = 0
for i in range(q):
    t, x = map(int, input().split())
    # キューの最後尾をキューの先頭に追加
    if t == 1:
        count += x
    # キューのx番目を表示
    else:
        index = (x - count) % n
        count %= n
        print(s[index - 1])
