import sys
import tracemalloc

tracemalloc.start()

input = sys.stdin.readline

num = int(input())
list = [0] * 1000000000

for i in range(num):
    a = i
    list[a-1] += 1

for i in range(10000):
    if list[i] != 0:
        for j in range(list[i]):
            print(i+1)
current,peak = tracemalloc.get_traced_memory()
print(f'{current / 1024 /1024:.2} MB')
print(f'{peak / 1024 /1024:.2} MB')