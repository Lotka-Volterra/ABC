n, a, b = map(int, input().split())
sum = 0
for i in range(1, n+1):
    l = len(str(i))
    ketasum = 0
    k = str(i)
    for j in range(l):
        ketasum += int(k[j])
    if a <= ketasum <= b:
        sum += i
print(sum)

# 文字に変換しない方法。iを別の変数tに保存し、それを10で割った余りを出す。そして、tを10で割る
# こうすることで、各桁を切り出せる。
n, a, b = map(int, input().split())
sum = 0
for i in range(1, n+1):
    t = i
    ketasum = 0
    #ここ、while t>0でもいい
    for j in range(5):
        ketasum += t % 10
        t //= 10
    if a <= ketasum <= b:
        sum += i
print(sum)
