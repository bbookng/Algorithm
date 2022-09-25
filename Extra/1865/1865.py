import sys
sys.stdin = open('input.txt')

def solution(i, total):
    global result
    if total < result:
        return

    if i == N:
        result = total
        return

    for idx in range(N):
        if candidates[idx] and arr[i][idx] != 0:
            candidates[idx] = 0
            solution(i+1, total * arr[i][idx] / 100)
            candidates[idx] = 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    candidates = [1] * N
    result = 0

    solution(0, 1)
    print(f'#{tc}', '{:.6f}'.format(result * 100))