N = input()
if N == "0000":
    print("SAME")
elif int(N) % 1111 == 0:
    print("SAME")
else:
    print("DIFFERENT")

# N=0000の場合、intにすると０なので、１つ目の分岐は不要。int(N)%1111 == 0:にまとめられる
