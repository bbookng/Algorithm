import sys
sys.stdin = open('1860.txt')

def sol(N, M, K, arr):
    arr.sort()
    for i in range(N):
        tmp = (arr[i] // M) * K - (i+1)
        if tmp < 0:
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {sol(N, M, K, arr)}')