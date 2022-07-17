n = int(input())
mochi = []
for i in range(n):
    mochi.append(int(input()))
mochi.sort(reverse=True)
mae = mochi[0]
dan = 1
for i in range(1, n):
    if mochi[i] < mae:
        mae = mochi[i]
        dan += 1
print(dan)

# この問題は、結局何通りの異なる値があるか？ということ。→集合を使えばいい
n = int(input())
mochi = []
for i in range(n):
    mochi.append(int(input()))
print(len(set(mochi)))
