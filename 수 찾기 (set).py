import sys

input = sys.stdin.readline

n_n = int(input())
n = set(map(int, input().split()))
m_n = int(input())
m = list(map(int, input().split()))
check = 0
for i in m:
    check = 0
    if i in n:
        check = 1
    print(check)
# left = 0
# right = len(m)

# for target in range(len(m)):
#     while left > right:
#         mid = (left + right) // 2
#         if n[mid] == m[target]:
#             check = 1
#             break
#         elif n[mid] < m[target]:
#             right = mid -1
#         else:
#             lef = mid + 1
#     print(check)