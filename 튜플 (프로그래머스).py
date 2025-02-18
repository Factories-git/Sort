def solution(s):
    answer = []
    tuple = s[2:-2].split('},{')
    tuple.sort(key= lambda x:len(x))
    for item in tuple:
        value = list(map(int, item.split(',')))
        for v in value:
            if v not in answer:
                answer.append(v)
    return answer
