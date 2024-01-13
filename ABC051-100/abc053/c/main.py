x = int(input())
# 貪欲に11を取り続けて、最後の調整として、mod 11 を取る。
# mod 11が6以下の場合、最初の得点が5か6かについて調整すればmod 11の値についてはサイコロ1回だけの回転で点数を得られる
# 11は5と6のセットでできるので、サイコロ2回分
shou = (x // 11) * 2
mod = x % 11
if mod == 0:
    print(shou)
elif 1 <= mod <= 6:
    print(shou + 1)
else:
    print(shou + 2)
