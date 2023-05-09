"""ビット全探索
N個の要素からいくつかを選択するケースに適用。
全探索で単純に実装すると、N重のfor文を書く必要があるが
ビット全探索だと簡略化出来る。

参考URL
https://qiita.com/gogotealove/items/11f9e83218926211083a
"""

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):  # 2の3乗 = 8 (from 0 to 7)
    bag = []
    amount = 0
    print("pattern {}: ".format(i), end="")
    for j in range(n):  # from 0 to 2
        # print("j", j)
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            amount += item[j][1]
    print(bag, amount)
