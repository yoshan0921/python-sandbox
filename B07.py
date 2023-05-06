import io
import sys

_INPUT = """\
10
7
0 10
2 4
1 3
0 3
5 6
5 6
0 1
"""
sys.stdin = io.StringIO(_INPUT)

close_time = int(input())
employees_num = int(input())
diff = [0] * (close_time + 1)

for i in range(employees_num):
    start, end = map(int, input().split())
    diff[start] += 1
    diff[end] -= 1

Answer = [0] * close_time
Answer[0] = diff[0]
for j in range(1, len(Answer)):
    Answer[j] = Answer[j-1] + diff[j]

for e, k in enumerate(Answer):
    print(e, k)
