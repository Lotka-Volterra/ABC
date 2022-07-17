a, b, k = map(int, input().split())
count = 0
for i in range(100):
    if a < b:
        count += 1
        a *= k
    else:
        print(count)
        quit()
print(count)

# 上は、上界が決まっており100ループ以内に終了するので、10行目は実行されない。
# whileを使う場合
a, b, k = map(int, input().split())
count = 0
while a < b:
    count += 1
    a *= k
print(count)
