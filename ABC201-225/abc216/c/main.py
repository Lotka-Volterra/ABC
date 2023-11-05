n = int(input())
reverseAnswer = ""
# nを0にする方法を探し、その逆順を答えとして出力する
# nが奇数なら1を引き、偶数なら2で割ることを繰り返す(たぶん貪欲)
while n > 0:
    if n % 2 == 1:
        n -= 1
        reverseAnswer += "A"
    else:
        n //= 2
        reverseAnswer += "B"
print("".join(list(reversed(reverseAnswer))))
