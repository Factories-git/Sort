s = int(input())
arr = list(map(int, input().split()))
count = 0
n = int(input())
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j]
            count += 1
print(arr)