s = input()
if int(s[5:7]) > 4:
    print("TBD")
else:
    print("Heisei")

# 文字列を数字と記号まじりの辞書式順序で比較する
S = input()
print('Heisei' if S <= '2019/04/30' else 'TBD')

# タプル同士の値の比較は、先頭の要素から順番に同じインデックス同士の値を比較して、先に小さい値となったタプルが小さい値になる。
ymd = tuple(map(int, input().split('/')))

if ymd <= (2019, 4, 30):
    print('Heisei')
else:
    print('TBD')
