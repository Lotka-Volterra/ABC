N = input()
if N == "A":
    print(1)
elif N == "B":
    print(2)
elif N == "C":
    print(3)
elif N == "D":
    print(4)
else:
    print(5)

#別解　ループで判定
S ="ABCDE"
for i in range(5):
    if S[i]==N:
        print(i+1)

#別解　文字コード
ans = ord(N) - ord('A')+1
print(ans)
