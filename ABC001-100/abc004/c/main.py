n = int(input())
shou = (n // 5) % 6
mod5 = n % 5
card = list(range(shou + 1, 7)) + list(range(1, shou + 1))
for i in range(mod5):
    cardI = card[i]
    card[i] = card[i + 1]
    card[i + 1] = cardI
ans = ""
for i in card:
    ans += str(i)
print(ans)
