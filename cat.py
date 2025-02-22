n = int(input())
s = [input() for i in range(n)]
s.sort(key=lambda x:len(x))
print(''.join(s))