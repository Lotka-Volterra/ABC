n = int(input())
for i in range(1, len(str(n))):
    if n % 10 != 0:
        break
    n //= 10
n = str(n)
for i in range(len(n)):
    if n[i] != n[-i - 1]:
        print("No")
        quit()
print("Yes")

# 公式解答
# N は高々10 桁なので、N の前につける 0 の個数は 9 個までを考慮すれば十分です。0 個から 9 個までそれぞれの場合について回文になるかどうかを判定すればよいです。
S=input()

for i in range(10):
	T = "0"*i + S
	if T==T[::-1]:
		print("Yes")
		exit()

print("No")
