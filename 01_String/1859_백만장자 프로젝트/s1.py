import sys
sys.stdin = open('1859.txt')

def sol(n, arr):
    result = arr[:]
    max_v = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_v:
            max_v = arr[i]
        result[i] = max_v
    return sum(result) - sum(arr)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {sol(n, arr)}')

