op = ['*', '']

for i in range(1000, 10000):
    c = str(i)
    for j in range(len(op)):
        for k in range(len(op)):
            for l in range(len(op)):
                if c[3] == '0':
                    break
                val = c[3] + op[j] + c[2] + op[k] + c[1] + op[l] + c[0]
                if not (len(val) <= 4 or '*0' in val):
                    if i == eval(val):
                        print(val + " = " + str(i))