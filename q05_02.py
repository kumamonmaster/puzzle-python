import itertools

coins = [10, 50, 100, 500]
cnt = 0

for i in range(2, 16):
    for coin_set in itertools.combinations_with_replacement(coins, i):
        if sum(coin_set) == 1000:
            cnt += 1

print(cnt)