n = int(input())
arr = list(map(int, input().split()))
s = int(input())
while True:
    br = True
    for i in range(n):
        max_ = i
        change = 0
        for j in range(n-1, i, -1):
            if arr[max_] < arr[j] and j-i <= s:
                max_ = j
                br = False
                change = j-i
        if max_ != i:
            t = arr.pop(max_)
            arr.insert(i, t)
            s -= change
    if br:
        break
print(*arr)