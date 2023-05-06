import io
import sys

_INPUT = """\
7
1 2 5 5 2 3 1
2
3 5
4 6
"""
sys.stdin = io.StringIO(_INPUT)

# Number of rooms
N = int(input())

# Capacity of each room
A = list(map(int, input().split()))
# print(A)

# Duration for construction
D = int(input())
# print(D)
L = [None] * D
R = [None] * D

for i in range(D):
    L[i], R[i] = map(int, input().split())

# print(L)
# print(R)

P = [None] * N
Q = [None] * N

P[0] = A[0]
# print(P)
for j in range(1, N):
    P[j] = max(P[j-1], A[j])

Q[N-1] = A[N-1]
# print(Q)
for k in reversed(range(0, N-1)):
    # print("k=" + str(k))
    Q[k] = max(Q[k+1], A[k])

# print(P)
# print(Q)

Answer = [0] * D
for l in range(D):
    # print("L[l]=" + str(L[l]))
    # print("R[l]=" + str(R[l]))
    print(max(P[(L[l]-1)-1], Q[(R[l]+1)-1]))
