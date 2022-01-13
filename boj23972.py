import math
K, N = map(int, input().split())

if N == 1:
    print(-1)
else:
    temp = K * N // (N - 1)
    if (K * N) % (N - 1):
        temp += 1
    print(temp)
