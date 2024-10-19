import sys

input = sys.stdin.readline

n_,m_ = map(int, input().split())

n = set()
m = set()

for i in range(n_):
    n.add(input().strip())
for i in range(m_):
    m.add(input().strip())
re = list()
for i in n:
    if i in m:
        re.append(i)
re.sort()
print(len(re))
for i in re:
    print(i)