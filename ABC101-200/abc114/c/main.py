import sys

sys.setrecursionlimit(100000000)


def sgs(number_string, digit):
    global ans
    # print(number_string)
    if number_string != "":
        if (
            int(number_string) <= n
            and "3" in number_string
            and "5" in number_string
            and "7" in number_string
        ):
            ans += 1
    for i in shichigosan:
        if int(number_string + i) > n:
            break
        sgs(number_string + i, digit)
    return None


n = int(input())
shichigosan = ["3", "5", "7"]
ans = 0
sgs("", int(len(str(n))))
print(ans)
