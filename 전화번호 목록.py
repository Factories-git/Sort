import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    t_c = int(input())
    arr = sorted([input().strip() for _ in range(t_c)])
    check = True
    for i in range(t_c-1):
        length = len(arr[i])
        if arr[i+1][:length] == arr[i]:
            check = False
            break
    print('YES' if check else 'NO')