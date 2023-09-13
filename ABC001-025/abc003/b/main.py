s = input()
t = input()
atcoder = "atcoder"
for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] == "@" and t[i] in atcoder:
            continue
        elif t[i] == "@" and s[i] in atcoder:
            continue
        else:
            print("You will lose")
            quit()
print("You can win")

# @とatcoderの判定の別解
# アルファベットおよび@についての連想配列を作成する。
# アルファベットはatcoderの文字だけが1点、@が10点（これは1点、-1点以外なら大きければなんでもいい）
# 文字を一つずつ比較するが、文字が等しくない場合、両者の文字の点数の和が11点あるいは0点ならcontinue、それ以外ならLoseをprintしてquit

# PyPyがメモリ超過（MLE）になったのでCPythonで提出