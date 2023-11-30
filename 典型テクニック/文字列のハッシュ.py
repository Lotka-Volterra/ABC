class RollingHash():
    def __init__(self, str, base=31, mod=10**9+7):
        # ハッシュ化する文字列全体
        self.str = str
        # 基数
        self.base = base
        # 割る数
        self.mod = mod
        # 文字列の長さ
        self.strlen = len(str)
        # 1文字目から、strlen文字目までの文字をあらかじめ数値に変換。aは1になる（０ではない）
        self.ordList = [0]*(self.strlen+1)
        for i in range(1, self.strlen+1):
            self.ordList[i] = ord(self.str[i-1])-ord('a')+1
        # 階乗の値のリスト、0乗からstrlen乗まで
        self.powerList = [1]*(self.strlen+1)
        for i in range(1, self.strlen+1):
            self.powerList[i] = (self.powerList[i-1]*self.base) % self.mod
        # 0からi文字目までのハッシュ値のリスト。hashList(0)=0,hashList(1)=str(1)のハッシュ値
        self.hashList = [0]*(self.strlen+1)
        for i in range(1, self.strlen+1):
            self.hashList[i] = (
                self.ordList[i]+self.hashList[i-1]*self.base) % self.mod

    # left文字目からright文字目までの文字列のハッシュ値を取得
    # str='a'だとright-left+1=1でindex out of rangeになるため、powerListはstrlen+1乗まである
    def get(self, left, right):
        return (self.hashList[right] - (self.hashList[left-1] * self.powerList[right-left+1]) % self.mod) % self.mod


n, q = map(int, input().split())
s = input()
# n進法の基数（=底）
base = 100
# modで割る値
mod = 2147483647
# mod = 10007
hash = RollingHash(s, base, mod)
for i in range(q):
    a, b, c, d = map(int, input().split())
    hashAB = hash.get(a, b)
    hashCD = hash.get(c, d)
    print('Yes' if hashAB == hashCD else 'No')
