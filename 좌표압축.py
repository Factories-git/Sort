import sys

input = sys.stdin.readline

n = int(input())

n_l = list(map(int, input().split()))

n_set = set(n_l)
asdf = list(n_set)
asdf.sort()

n_d = dict()

for i in range(len(asdf)):
    n_d[asdf[i]] = i

for i in n_l:
    print(n_d[i], end=' ')
