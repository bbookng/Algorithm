import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])

    tmp = 0
    cnt = 0

    for s, e in arr:
        if s >= tmp:
            cnt += 1
            tmp = e

    print(f'#{tc} {cnt}')