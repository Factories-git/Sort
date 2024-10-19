import sys

input = sys.stdin.readline

l = []
for i in range(int(input())):
    l.append([int(input()), i])
sorted_l = sorted(l)
ans = []
for i in range(len(l)):
    ans.append(sorted_l[i][1] - l[i][1])
print(max(ans)+1)