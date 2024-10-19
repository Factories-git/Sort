import sys

input = sys.stdin.readline

id = []
for i in range(int(input())):
    age,name = list(map(str, input().split()))
    id.append([int(age),i,name])
id.sort()
for i in id:
    print(i[0],i[2])