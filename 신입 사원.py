import sys, heapq

input = sys.stdin.readline

for _ in range(int(input())):
    number = []
    one = []
    heapq.heapify(one)
    scores = []
    re = 0
    n = int(input())
    for j in range(n):
        document, interview = map(int, input().split())
        scores.append([document, interview])
    scores.sort()
    cutLine = [100001, 100001]
    for d, i in scores:
        if cutLine[0] >= d or cutLine[1] >= i:
            cutLine = [d, i]
            re += 1
    print(re)
