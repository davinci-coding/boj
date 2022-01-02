C, R = map(int, input().split())
K = int(input())

stage = [[0 for _ in range(R)] for _ in range(C)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 1
y = C - 1
x = 0
stage[y][x] = cnt
while cnt < K:
    cnt += 1
    if state[y][x] != 0:

