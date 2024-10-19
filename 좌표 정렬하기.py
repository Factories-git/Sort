import sys

input  = sys.stdin.readline

coordinate = []
for i in range(int(input())):
    coordinate.append(list(map(int, input().split())))
re = sorted(coordinate)
for i in re:
    print(f'{i[0]} {i[1]}')