n = int(input())
time = input().split()
re = sorted(time)
answer2 = 0
answer = 0
for i in re:
    answer2 += int(i)
    answer += answer2
print(answer)