#round는 구현하자
import sys

input = sys.stdin.readline


def myRound(num):
    s = num - int(num)

    if s >= 0.5:
        return int(num) + 1
    elif s < 0.5:
        return int(num)


n = int(input())
difficulty = 0
if n == 0:
    print(0)
    exit(0)
opinions = []
for i in range(n):
    opinions.append(int(input()))
opinions.sort()
cutoff = myRound((15 / 100) * n)

if cutoff == 0:
    print(myRound(sum(opinions) / n))
    exit(0)
opinions = opinions[cutoff:-cutoff]
division = n - (2 * cutoff) if (n - (2 * cutoff)) != 0 else n
print(myRound(sum(opinions) / division))
