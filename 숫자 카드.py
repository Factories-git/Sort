import sys

input = sys.stdin.readline

n_n = int(input())
n = set(map(int, input().split()))
m_n = int(input())
m = list(map(int, input().split()))
check = 0
string = []
for i in m:
    check = 0
    if i in n:
        check = 1
    string.append(check)
print(' '.join(map(str,string)))