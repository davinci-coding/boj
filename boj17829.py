N = int(input())

def pulling(n, y, x):
    if n == 2:
        arr = [matrix[y][x], matrix[y][x+1], matrix[y+1][x], matrix[y+1][x+1]]
        arr.sort()
        return arr[-2]
    
    half = n // 2
    lt = pulling(half, y, x)
    rt = pulling(half, y, x + half)
    lb = pulling(half, y + half, x)
    rb = pulling(half, y + half, x + half)

    arr = [lt, rt, lb, rb]
    arr.sort()
    return arr[-2]

matrix = [list(map(int, input().split())) for _ in range(N)]

print(pulling(N, 0, 0))