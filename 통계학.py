import sys


input = sys.stdin.readline

def solution(array):
    from collections import Counter

    counter = Counter(array)

    max_count = max(counter.values())

    max_values = [k for k,v in counter.items() if v == max_count]
    max_values.sort()
    answer = max_values[0]
    if len(max_values) > 1:
        answer = max_values[1]
    return answer
array = []
for i in range(int(input())):
    array.append(int(input()))
array.sort()
print(round(sum(array)/len(array)))
print(array[len(array)//2])
print(solution(array))
print(array[-1] - array[0])