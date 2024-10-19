score = []
for i in range(int(input())):
    scores = list(map(int, input().split()))
    s = max(scores[:2])
    sco = sorted(scores[2:], reverse=True)
    score.append(s + sco[0]+sco[1])
print(max(score))