n = input()
for i in range(2):
    if n[i] == "9":
        print("Yes")
        exit()
print("No")

# 別解：各位の数字を数字のまま比較
n = int(input())
if n % 10 == 9 or n//10 == 9:
    print("Yes")
else:
    print("No")

# 別解：文字列中に数字９が含まれているか
n = input()
if "9" in n:
    print("Yes")
else:
    print("No")
