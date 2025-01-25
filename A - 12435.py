
a = list(map(int, input().split()))
if sorted(a) == a:
    print('No')
    exit(0)
for idx, i in enumerate(a):
    if abs(idx+1 - i) > 1:
        print('No')
        exit(0)
print('Yes')