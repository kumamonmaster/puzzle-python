def cut_bar(m, n):
    count = 0
    current = 1 # 現在の棒の長さ

    while n > current:
        current += current if current < m else m
        count += 1
    return count

print(cut_bar(3, 20))
print(cut_bar(5, 100))