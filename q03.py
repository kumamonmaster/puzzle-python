# パターン1
N = 100
cards = [False for i in range(N)]

for i in range(2, N+1):
    j = i -1
    while j < len(cards):
        cards[j] = not cards[j]
        j += i

for i, card in enumerate(cards):
    if not card:
        print(i+1)

# パターン2
# for i in range(1, 101):
#     flag = False
#     for j in range(1, 101):
#         if i % j == 0:
#             flag = not flag
#     if flag:
#         print(i)