num = 11

while True:
    # 8進数
    num_o = format(num, 'o')
    # 2進数
    num_b = format(num, 'b')

    if str(num) == str(num)[::-1] and num_o == num_o[::-1] and num_b == num_b[::-1]:
        print('10進数: ' + str(num) + '\n8進数: ' + str(num_o) + '\n2進数: ' + str(num_b))
        break

    num += 2