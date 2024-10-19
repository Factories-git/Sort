def solution(numbers):
    answer = ''
    n_s_l = [str(i) for i in numbers]

    n_s_l.sort(key=lambda i : i*10, reverse=True)
    answer = str(int(''.join(n_s_l)))

    return answer
q = int(input())
numbers = list(map(int, input().split()))
print(solution(numbers))
