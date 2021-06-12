'''
長さn[cm]の1本の棒を1[cm]単位に切り分けることを考えます。ただし、1本の棒を一度に切ることができるのは1人だけです。
切り分けられた棒が3本あれば、同時に3人で切ることができます。

最大m人の人がいるとき、最短何回で切り分けられるかを求めてください。
例えば、n=8, m=3のときは、4回で切り分けることができます。

n = 20, m = 3のときの回数を求めてください。
n = 100, m = 5のときの回数を求めてください。
'''

def cut_bar(m, n, current):
    if current >= n:
        return 0
    elif current < m:
        return 1 + cut_bar(m, n, current * 2)
    else:
        return 1 + cut_bar(m, n, current + m)

print(cut_bar(3, 20, 1))
print(cut_bar(5, 100, 1))