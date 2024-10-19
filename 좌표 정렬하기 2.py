import sys

input  = sys.stdin.readline

coordinate = []
for i in range(int(input())):
    ipt = list(map(int, input().split()))
    coordinate.append([ipt[1], ipt[0]])
re = sorted(coordinate)
for i in re:
    print(f'{i[1]} {i[0]}')