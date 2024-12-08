import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = list()
for i in range(n):
    ipt = input().strip()
    if len(ipt) >= m:
        words.append(ipt)
words = list(words)
c = Counter(words)
new_words = set()
for i in range(len(words)):
    new_words.add((words[i], c[words[i]], len(words[i])))

new_words = sorted(new_words, key= lambda x: (-x[1], -x[2], x[0]))
for i in new_words:
    print(i[0])