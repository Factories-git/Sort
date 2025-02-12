from collections import Counter
def solution(X, Y):
    answer = ''
    answer_l = []
    n_l = [str(i) for i in range(10)][::-1]
    nums = {'0':[0,0] ,'1' : [0,0], '2':[0,0], '3':[0,0], '4':[0,0], '5':[0,0], '6':[0,0], '7':[0,0], '8':[0,0], '9':[0,0], '10':[0,0]}
    for i in X:
        nums[i][0] += 1
    for j in Y:
        nums[j][1] += 1
    for i in n_l:
        for j in range(min(nums[i])):
            answer += i
    if not answer:
        return '-1'
    return str(int(answer))

print(solution(	"100", "203045"))