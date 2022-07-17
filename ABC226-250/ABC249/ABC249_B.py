S = input()

#すべて大文字でもなく、すべて小文字でもない場合にOmojiフラグがTrueになる
if S.islower() or S.isupper():
    Omojiflg = False
else:
    Omojiflg = True

#OmojiフラグがTrueの場合、同じ文字を含んでいないか調査
if Omojiflg:
    # iは文字列の末尾−１まで。文字列の末尾だと比較対象が無い
    for i in range(len(S)-1):
        #自分自身を含めないように、jはiより大きいインデックス
        for j in range(i+1,len(S)):
            #同じ文字を含んでいるならFalseになって抜け出す
            if S[i] == S[j]:
                Omojiflg = False
                break
        #OmojiフラグがFalseになっていたら繰り返す意味もないので抜け出す
        if not(Omojiflg):
            break

if Omojiflg:
    print("Yes")
else:
    print("No")