import sys

input = sys.stdin.readline

n_n = int(input())
n = list(map(int, input().split()))
m_n = int(input())
m = list(map(int, input().split()))
check = dict()
a = []
for i in n:
    try:
        check[i] += 1
    except:
        check[i] = 1
for i in m:
    try:
        a.append(check[i])
    except:
        a.append(0)
print(' '.join(map(str, a)))