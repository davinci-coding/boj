cnt = 0
max_val = 0

for i in range(9):
    n = int(input())
    if max_val < n:
        max_val = n
        cnt = i

print(max_val)
print(cnt+1)