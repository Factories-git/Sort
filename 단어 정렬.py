import sys

str_set = set()
for i in range(int(input())):
    word = sys.stdin.readline().split()[0]
    str_set.add(word)
sorted_list = []
for i in str_set:
    sorted_list.append([len(i),i])
sorted_list = sorted(sorted_list)
for i in sorted_list:
    print(i[1])