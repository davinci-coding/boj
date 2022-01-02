m = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

def w(a, b, c):
    if m[a + 50][b + 50][c + 50]:
        return m[a+50][b+50][c+50]

    if a <= 0 or b <= 0 or c <= 0:
        m[a+50][b+50][c+50] = 1
        return 1
    
    if a > 20 or b > 20 or c > 20:
        m[a+50][b+50][c+50] = w(20, 20, 20)
        return m[a+50][b+50][c+50]
    
    if a < b and b < c:
        m[a+50][b+50][c+50] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return m[a+50][b+50][c+50]


    m[a+50][b+50][c+50] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return m[a+50][b+50][c+50] 

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")