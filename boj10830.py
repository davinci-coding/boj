N, B = map(int, input().split())

my_list = [list(map(int, input().split())) for _ in range(N)]

def mul(n, m1, m2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= 1000
    return result

def DnC(n, b, ml):
    if b == 1:
        return ml
    elif b == 2:
        return mul(n, ml, ml)
    else:
        tmp = DnC(n, b//2, ml)
        if b % 2:
            return mul(n, mul(n, tmp, tmp), ml)
        else:
            return mul(n, tmp, tmp)

result = DnC(N, B, my_list)

for row in result:
    for n in row:
        print(n % 1000, end=' ')
    print()
