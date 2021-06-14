"""
1000円札を入れたときに出てくる硬貨の組み合わせは何通りあるかを求めてください。
なお、硬貨の順番は区別しないものとします。
"""

cnt = 0
for coin500 in range(3):
    for coin100 in range(11):
        for coin50 in range(16):
            for coin10 in range(16):
                if coin500 + coin100 + coin50 + coin10 <= 15:
                    if coin500 * 500 + coin100 * 100 + coin50 * 50 + coin10 * 10 == 1000:
                        cnt += 1

print(cnt)