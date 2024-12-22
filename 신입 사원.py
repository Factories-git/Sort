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
        number.append(document + interview)
        scores.append([document + interview, document, interview])
        if document == 1 or interview == 1:
            heapq.heappush(one, [(document + interview), document, interview])
            if document == interview == 1:
                heapq.heappush(one, [(document + interview), document, interview])
    scores.sort()
    for s, d, i in scores:
        if d == 1 or i == 1:
            re += 1
            if d == i == 1:
                one.append([s, d, i])
            one.append([s, d, i])
        else:
            if (s <= one[1][0] or s <= one[0][0]) and (d < one[1][1] and i < one[0][2]):
                re += 1
    print(re)
