k = int(input())
ans = ""
for i in range(k):
    ans += chr(ord("A") + i)
print(ans)

# Python の標準ライブラリには、A から Z までの文字を昇順に繋げた文字列が 
# string.ascii_uppercase として入っています。
# これを用いると非常に簡潔な実装が得られます。
import string

print(string.ascii_uppercase[:int(input())])
