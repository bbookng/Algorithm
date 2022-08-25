import sys
sys.stdin = open('5099.txt')

def sol(N, arr):
    now = [arr.pop(0) for _ in range(N)]
    while len(now) != 1:
        idx, pizza = now.pop(0)
        pizza //= 2
        if pizza:
            now.append((idx, pizza))
        elif arr:
            now.append(arr.pop(0))
    return now[0][0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in enumerate(map(int, input().split()), 1):
        arr.append(i)
    print(f'#{tc} {sol(N, arr)}')