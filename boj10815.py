import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

card.sort()
def binary_search(target, start, end):
    global card
    while start <= end:
        mid = (start + end) // 2
        if target == card[mid]:
            return mid
        elif target < card[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

for i in check:
    rst = binary_search(i, 0, N-1)
    if rst is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')



